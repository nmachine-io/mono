require 'kerbi'

class MainMixer < Kerbi::Mixer

  def run
    super do |g|
      if values[:strategy] == 'single-secret'
        g.yaml 'single-secret'
      elsif values[:strategy] == 'multi-secret'
        g.yaml 'multi-secret'
      end
    end
  end

  def flat_secrets_mapping
    Kerbi::Utils::Utils.flatten_hash(values[:secrets] || {})
  end

  def strategy
    values[:strategy]
  end

  def b64enc_or_plain(val)
    values[:b64_enc] ? b64enc(val) : val
  end

end

kerbi.generators = [ MainMixer ]
puts kerbi.cli_exec