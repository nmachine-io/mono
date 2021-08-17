require_relative './../common'

class MonolithMixer < Kerbi::Mixer
  include Common

  locate_self __dir__

  def run
    super do |t|
      t.yaml 'pvc'
      t.yaml 'pg-deployment', extras: postgres_extras
      t.yaml generic('service'), extras: postgres_extras
      t.yaml generic('deployment'), extras: deployment_extras
      t.yaml generic('service'), extras: service_extras
    end
  end

  def deployment_extras
    root = deployment_values_root
    init_container = container_config(root, 'db-init', 'rake db:init')
    main_container = container_config(root, 'main', 'rails server')
    {
      name: consts.backend_name,
      root: root,
      init_containers: [init_container],
      containers: [main_container]
    }
  end

  def container_config(root, name, command)
    extras = {
      name: name,
      command: command,
      env_vars: templated_env_vars,
      root: root,
      service_root: service_values_root
    }
    self.inflate_yaml_file('backend-container', [], [], extras).first
  end

  def templated_env_vars
    self.inflate_yaml_file('env_vars', [], [], {})
  end

  def generic(name)
    "./../generic/#{name}"
  end

  def postgres_extras
    {
      root: { port: 5432 },
      name: consts.postgres_name
    }
  end

  def service_extras
    {
      name: consts.backend_name,
      root: service_values_root
    }
  end

  def deployment_values_root
    values.dig(consts.backend_name.to_sym, :deployment) || {}
  end

  def service_values_root
    values.dig(consts.backend_name.to_sym, :service) || {}
  end
end