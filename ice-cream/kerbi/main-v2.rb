require 'kerbi'

class MainMixer < Kerbi::Mixer
  locate_self __dir__

  def run
    super do |g|
      g.yaml 'manifest-v2'
    end
  end
end

kerbi.generators = [ MainMixer ]
puts kerbi.cli_exec