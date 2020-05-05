require 'kerbi'
require_relative 'gen'

kerbi.generators = [ Hub::Gen ]

puts kerbi.gen_yaml