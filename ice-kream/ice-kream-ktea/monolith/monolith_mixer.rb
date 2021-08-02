require_relative './../common'

class MonolithMixer < Kerbi::Mixer
  include Common

  locate_self __dir__

  def run
    super do |t|
      t.yaml 'pvc'
      t.yaml 'pg-deployment', extras: postgres_bundle
      t.yaml generic('service'), extras: postgres_bundle
      t.yaml generic('deployment'), extras: deployment_extras
      t.yaml generic('service'), extras: monolith_service_extras
    end
  end

  def monolith_service_extras
    {
      name: consts.backend_name,
      root: backend_deployment_values_root
    }
  end

  def deployment_extras
    root = backend_deployment_values_root
    {
      name: consts.backend_name,
      root: root,
      init_containers: [container_config(root, 'db-init', 'rake db:init') ],
      containers: [container_config(root, 'main', 'rails server') ]
    }
  end

  def backend_deployment_values_root
    values.dig(*consts.backend_name.to_sym) || {}
  end

  def container_config(root, name, command)
    extras = {
      name: name,
      command: command,
      env_vars: templated_env_vars,
      root: root
    }
    self.inflate_yaml_file('backend-container', [], [], extras).first
  end

  def templated_env_vars
    self.inflate_yaml_file('env_vars', [], [], {})
  end

  def generic(name)
    "./../generic/#{name}"
  end

  def postgres_bundle
    {
      root: { port: 5432 },
      name: consts.postgres_name
    }
  end

  def backend_server_bundle
    {
      root: backend_deployment_values_root,
      name: consts.backend_name
    }
  end
end