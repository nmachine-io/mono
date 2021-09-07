import os

from custom.v2_virtual_ktea import V2VirtualKtea
from kama_sdk.cli import entrypoint
from kama_sdk.core.core.plugins_manager import plugins_manager
from kama_sdk.core.ktea.virtual_ktea_client import vktea_clients_manager
from kama_sdk.core.telem.telem_manager import telem_manager
from kama_sdk.model.base.model import models_manager
from kama_sdk.utils.descriptor_utils import load_dir_yamls
from kama_telem_plugin import plugin as telem_plugin
from kama_telem_plugin.nmachine_telem_backend import NMachineTelemBackend


def register_own_artifacts():
  root_dir = os.path.dirname(os.path.abspath(__file__))
  descriptors = load_dir_yamls(f'{root_dir}/descriptors')
  models_manager.add_descriptors(descriptors)
  models_manager.add_asset_dir_paths([f'{root_dir}/assets'])


def register_examples():
  hack_root_dir = os.path.expanduser("~/workspace/kama-sdk-py")
  descriptors = load_dir_yamls(f'{hack_root_dir}/examples/descriptors')
  models_manager.add_descriptors(descriptors)


def register_plugins():
  plugins_manager.register(manifest=telem_plugin.get_manifest())


def register_delegates():
  vktea_clients_manager.register_client(V2VirtualKtea)
  telem_manager.set_backend_class(NMachineTelemBackend)


if __name__ == '__main__':
  register_own_artifacts()
  register_examples()
  register_delegates()
  register_plugins()
  entrypoint.start()


TELEM_PLUGIN_ID = "nmachine.telemetry"
