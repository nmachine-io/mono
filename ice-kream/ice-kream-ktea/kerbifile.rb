require_relative 'consts'
require_relative 'monolith/network_mixer'
require_relative 'monolith/configs_mixer'
require_relative 'monolith/monolith_mixer'

class HelloWorld < Kerbi::Mixer
  def mix
    push mixer(ConfigsMixer)
    push mixer(MonolithMixer)
    push mixer(NetworkMixer)
  end
end

Kerbi::Globals.mixers << HelloWorld