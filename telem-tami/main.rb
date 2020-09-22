require 'kerbi'

class MainMixer < Kerbi::Mixer
  locate_self __dir__

  def run
    super do |g|
      g.yaml 'manifest'
    end
  end

  def redis_secret
    @_sec ||= Base64.encode64(SecureRandom.hex(10))
  end
end

kerbi.generators = [ MainMixer ]
puts kerbi.cli_exec