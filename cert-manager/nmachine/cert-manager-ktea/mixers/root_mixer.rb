class RootMixer < Kerbi::Mixer
  locate_self __dir__
  def run
    super do |k|
      k.yaml "manifest"
    end
  end
end

