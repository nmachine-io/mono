class NetworkMixer < Kerbi::Mixer

  locate_self __dir__

  def mix
    push file('ingress') if ingress_enabled?
  end

  def translate(name)
    if name.to_s == Constants.backend_name
      port = values.dig(Constants.backend_name, :service_port) || '3000'
      { name: name,  port: port }
    else
      port = (values.dig(name.to_sym) || {})[:port]
      { name: name.to_s.gsub('_', '-'),  port: port }
    end
  end

  def defined_routes
    routes_hash = self.values.dig(:ingress, :routes) || {}

    defined_routes_hash = routes_hash.reject do |_, route|
      important_values = route.values_at(:host, :path)
      important_values.reject(&:present?).any?
    end

    defined_routes_hash.map do |key, route|
      route.merge(
        name: key,
        service_name: translate(key)[:name],
        service_port: translate(key)[:port]
      )
    end
  end

  def ingress_enabled?
    values.dig(:ingress, :enabled).to_s == 'true'
  end
end