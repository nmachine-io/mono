import os

from kama_sdk.cli import entrypoint
from kama_sdk.core.core.plugins_manager import plugins_manager
from kama_sdk.model.base.model import models_manager
from kama_sdk.utils.descriptor_utils import load_dir_yamls
# from kama_sdk.core.telem.telem_manager import telem_manager
from cert_manager_plugin import plugin as cert_manager_plugin
# from kama_prom_plugin import plugin as prom_plugin
# from kama_telem_plugin import plugin as telem_plugin
# from kama_telem_plugin.nmachine_telem_backend import NMachineTelemBackend


def register_own_artifacts():
  root_dir = os.path.dirname(os.path.abspath(__file__))
  descriptors = load_dir_yamls(f'{root_dir}/descriptors')
  models_manager.add_descriptors(descriptors)
  models_manager.add_asset_dir_paths([f'{root_dir}/assets'])


def register_plugins():
  # plugins_manager.register(manifest=telem_plugin.get_manifest())
  # plugins_manager.register(manifest=prom_plugin.get_manifest())
  plugins_manager.register(manifest=cert_manager_plugin.get_manifest())


if __name__ == '__main__':
  register_own_artifacts()
  register_plugins()
  entrypoint.start()
