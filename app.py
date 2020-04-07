from moz.mosaic_wizard import MosaicWizard
from wiz import server

from wiz.core.base_adapter import PythonBackend

server.start(
  MosaicWizard,
  PythonBackend
)

print("Exec'ed")
