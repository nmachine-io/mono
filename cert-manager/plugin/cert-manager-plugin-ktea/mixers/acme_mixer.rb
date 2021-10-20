class AcmeMixer < Kerbi::Mixer

  locate_self __dir__

  def run
    super do |k|
      k.yaml 'acme_issuer', extras: extras
    end
  end

  def extras
    {
      name: values.dig(:issuer, :name),
      root: values[:acme]
    }
  end

end