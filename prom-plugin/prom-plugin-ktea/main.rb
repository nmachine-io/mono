require 'kerbi'

class PromMixer < Kerbi::Mixer
	locate_self __dir__
	def run
		{}
	end
end

kerbi.generators = [ PromMixer ]
puts kerbi.cli_exec