require "kerbi"

class MainMixer < Kerbi::Mixer
	def run
		super do |bucket|
			bucket.http manifest
		end
	end
end


cli.go

manifest = "https://github.com/jetstack/cert-manager/releases/download/v1.5.3/cert-manager.yaml"
