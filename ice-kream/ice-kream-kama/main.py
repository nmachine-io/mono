import os

from kama_sdk.cli import entrypoint
from kama_sdk.model.base.model import models_manager
from kama_sdk.utils.descriptor_utils import load_dir_yamls


def register_self():
  root_dir = os.path.dirname(os.path.abspath(__file__))
  descriptors = load_dir_yamls(f'{root_dir}/descriptors')

  models_manager.add_descriptors(descriptors)
  models_manager.add_asset_dir_paths([f'{root_dir}/assets'])


def register_plugins():
  pass
  # plugins_manager.register('telem_kaml')
  # plugins_manager.register('prom_kaml')


if __name__ == '__main__':
  # register_libraries()
  register_self()
  entrypoint.start()
