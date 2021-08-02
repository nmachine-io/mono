module Common

  def consts
    Constants
  end

  def globals
    @_globals_computer ||= Globals.new(values: self.values)
  end

  def app_name
    self.consts.app_name
  end
end
