require 'kerbi'
require_relative 'gen'

kerbi.generators = [ Hub::Gen ]

puts "Kerbi gave me values"

kerbi.values

puts kerbi.gen_yaml