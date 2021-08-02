require 'kerbi'
require 'active_support/core_ext/object/blank.rb'
require_relative 'consts'
require_relative 'common'
require_relative 'monolith/monolith_mixer'
require_relative 'monolith/network_mixer'
require_relative 'monolith/configs_mixer'

kerbi.generators = [ConfigsMixer, MonolithMixer, NetworkMixer]
kerbi.cli_exec