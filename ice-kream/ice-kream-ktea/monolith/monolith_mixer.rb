
class MonolithMixer < Kerbi::Mixer

  locate_self __dir__

  def mix
    push file('pvc')
    push file('pg-deployment', extras: postgres_extras)
    push file(generic("service"), extras: postgres_extras)
    push file(generic("deployment"), extras: deployment_extras)
    # t.yaml generic('service'), extras: postgres_extras
    # t.yaml generic('deployment'), extras: deployment_extras
    # t.yaml generic('service'), extras: service_extras
  end

  def deployment_extras
    root = deployment_values_root
    init_container = container_config(root, 'db-init', 'rake db:init')
    main_container = container_config(root, 'main', 'rails server')
    {
      name: Constants.backend_name,
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
    file('backend-container', extras: extras).first
  end

  def templated_env_vars
    file('env_vars')
  end

  def generic(name)
    "./../generic/#{name}"
  end

  def postgres_extras
    {
      root: { port: 5432 },
      name: Constants.postgres_name
    }
  end

  def service_extras
    {
      name: Constants.backend_name,
      root: service_values_root
    }
  end

  def deployment_values_root
    values.dig(Constants.backend_name.to_sym, :deployment) || {}
  end

  def service_values_root
    values.dig(Constants.backend_name.to_sym, :service) || {}
  end
end