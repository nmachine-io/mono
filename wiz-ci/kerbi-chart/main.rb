require 'kerbi'

class SimpleMixer < Kerbi::Mixer
  locate_self __dir__
  def run
    super { |res| res.yaml 'res' }
  end
end

kerbi.generators = [ SimpleMixer ]

kerbi.cli_exec