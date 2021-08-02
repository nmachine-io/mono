class ConfigsMixer < Kerbi::Mixer
  include Common

  locate_self __dir__

  def run(&block)
    super do |t|
      standard_secret_bundles.each do |bundle|
        t.yaml 'generic-secret', extras: bundle
      end
    end
  end

  def standard_secret_bundles
    all_roots = values.dig(:secrets, :standard)
    roots = all_roots.select do |_, r|
      r&.values.map(&:presence).compact.any?
    end
    root2extras(roots)
  end

  def root2extras(roots)
    roots.map do |key, data|
      secret_name = key.to_s.gsub('_', '-')
      { secret_name: secret_name, data: data }
    end
  end
end