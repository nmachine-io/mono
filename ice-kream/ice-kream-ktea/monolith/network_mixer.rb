class NetworkMixer < Kerbi::Mixer
  include Common

  locate_self __dir__

  def run
    super do |t|
      t.yaml 'certs' if ingress_enabled?
      t.yaml 'ingress' if ingress_enabled?
    end
  end

  def translate(name)
    if name.to_s == consts.backend_name
      port = values.dig(consts.backend_name, :service_port) || '3000'
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