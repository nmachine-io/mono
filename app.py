import moz
from moz import concerns
from moz.core.mosaic_wizard import MosaicWizard
from wiz import server

from wiz.core.base_adapter import PythonBackend
from wiz.core.wiz_globals import wiz_globals

wiz_globals.package_base = moz
wiz_globals.concerns_package = concerns

wiz_globals.set_concerns_package(concerns)

server.start(
  MosaicWizard,
  PythonBackend
)

print("Exec'ed")
