require 'kerbi'
require_relative 'mixers/root_mixer'
require_relative 'mixers/acme_mixer'

kerbi.generators = [RootMixer]
kerbi.cli_exec