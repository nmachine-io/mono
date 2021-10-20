class RootMixer < Kerbi::Mixer
  def run
    super do |k|
      case values.dig(:issuer, :type)
      when 'acme'
        k.mixer AcmeMixer
      else
        # nothing
      end
    end
  end
end
