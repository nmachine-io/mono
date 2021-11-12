require 'kerbi'
require_relative 'mixers/root_mixer'

kerbi.generators = [RootMixer]
kerbi.cli_exec