require 'active_support/core_ext/object/blank.rb'

module Hub
  class Gen < Kerbi::Gen

    locate_self __dir__

    def gen
      safe_gen do |res|
        res.yaml 'foundation'
        res.yaml 'pvc' if managed_pvc?
        if secrets_ready?
          res.yaml 'secrets'
          res.yaml 'pg' if internal_storage?
          res.hash build_deployment
        end
        res.hash build_service
      end
    end

    def build_deployment
      Kerbi::DeploymentTemplate.generic(
        name: "hub",
        ns:  'hub',
        init_containers: [ build_container('db-init', 'rake db:init')],
        containers: [ build_container('main', 'rails server') ]
      )
    end

    def build_service
      Kerbi::ServiceTemplate.generic_service(
        name: 'hub',
        ns: 'hub',
        type: values[:app][:service_type],
        ports: [ 3000 ]
      )
    end

    def build_container(name, cmd)
      Kerbi::DeploymentTemplate.container(
        name: name,
        image: "gcr.io/nectar-bazaar/hub:latest",
        cmd: "bundle exec #{cmd}",
        envs: build_container_env,
        image_pull_policy: 'Always'
      )
    end

    def build_container_env
      Kerbi::EnvVarTemplate.generics(
        database_host: 'postgres',
        database_port: '5432',
        rails_env: 'production',
        rails_log_to_stdout: 'true',
        database_user: { secret: { 'hub-pg': 'user' } },
        database_password: { secret: { 'hub-pg': 'password' } },
        secret_key_base: { secret: { 'hub-app': 'secret-key-base' } }
      )
    end

    def internal_storage?
      values[:storage][:type] == 'internal'
    end

    def managed_pvc?
      internal_storage? && values[:storage][:managed_pvc]
    end

    def pg_secret_ready?
      begin
        root = values[:storage][:secrets]
        root[:user].present? && root[:password].present?
      rescue
        false
      end
    end

    def app_secret_ready?
      values[:app][:secrets][:key_base].present? rescue false
    end

    def secrets_ready?
      pg_secret_ready? && app_secret_ready?
    end
  end
end