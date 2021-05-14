import os

from kama_sdk import entrypoint
from kama_sdk.model.base.model import models_man
from kama_sdk.core.core import utils, kaml_man
from prom_kaml.kaml import PromKaml
from telem_kaml.kaml import TelemKaml


def register_self():
  root_dir = os.path.dirname(os.path.abspath(__file__))
  yamls = utils.yamls_in_dir(f'{root_dir}/configs', recursive=True)
  models_man.add_descriptors(yamls)


def register_libraries():
  kaml_man.register_kaml(TelemKaml)
  kaml_man.register_kaml(PromKaml)


if __name__ == '__main__':
  register_libraries()
  register_self()
  entrypoint.start()
