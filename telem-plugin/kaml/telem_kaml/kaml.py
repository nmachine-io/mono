import os
from typing import List, Dict

from kama_sdk.core.core.kaml import KamlDescriptor
from kama_sdk.core.core import utils
from telem_kaml.telem_backend import TelemPluginBackend


def describe_self() -> KamlDescriptor:
  return KamlDescriptor(
    id='nmachine.telem',
    publisher_identifier='nmachine',
    app_identifier='telem-plugin',
    model_descriptors=model_descriptors(),
    asset_paths=[assets_path],
    model_classes=[],
    telem_backend=TelemPluginBackend,
    virtual_kteas=[]
  )


def model_descriptors() -> List[Dict]:
  return utils.yamls_in_dir(yamls_path, recursive=True)


root_dir = os.path.dirname(os.path.abspath(__file__))
yamls_path = f'{root_dir}/yamls'
assets_path = f'{root_dir}/assets'
