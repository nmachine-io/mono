require 'kerbi'

class TelemMixer < Kerbi::Mixer
	locate_self __dir__

	def run
		super do |b|
			if enabled?
				b.yaml 'pvc' if pvc?
				b.yaml 'deployment'
				b.yaml 'service'
				# b.yaml "backup-job"
			end
		end
	end

	def final_host
		pvc? ? 'localhost' : values.dig(:mongo, :host)
	end

	def final_port
		pvc? ? '27017' : values.dig(:mongo, :port)
	end

	def name
		values[:name]
	end

	def org
		values[:org]
	end

	def enabled?
		!!values[:enabled]
	end

	def pvc?
		values[:strategy] == 'pvc'
	end
end

kerbi.generators = [ TelemMixer ]
puts kerbi.cli_exec