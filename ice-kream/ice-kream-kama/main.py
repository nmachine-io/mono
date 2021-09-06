import os

from custom.v2_virtual_ktea import V2VirtualKtea
from kama_sdk.cli import entrypoint
from kama_sdk.core.ktea.virtual_ktea_client import vktea_clients_manager
from kama_sdk.model.base.model import models_manager
from kama_sdk.utils.descriptor_utils import load_dir_yamls


def register_self():
  root_dir = os.path.dirname(os.path.abspath(__file__))
  descriptors = load_dir_yamls(f'{root_dir}/descriptors')
  models_manager.add_descriptors(descriptors)

  models_manager.add_asset_dir_paths([f'{root_dir}/assets'])


def register_examples():
  root_dir = os.path.expanduser("~/workspace/kama-sdk-py")
  descriptors = load_dir_yamls(f'{root_dir}/examples/descriptors')
  models_manager.add_descriptors(descriptors)


def register_virtual_kteas():
  vktea_clients_manager.register_client(V2VirtualKtea)


def register_plugins():
  pass
  # plugins_manager.register('telem_kaml')
  # plugins_manager.register('prom_kaml')


if __name__ == '__main__':
  # register_libraries()
  register_self()
  register_examples()
  register_virtual_kteas()
  entrypoint.start()
