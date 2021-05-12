import os

from kama_sdk import entrypoint
from kama_sdk.model.base.model import models_man
from kama_sdk.core.core import utils

if __name__ == '__main__':
  root_dir = os.path.dirname(os.path.abspath(__file__))
  yamls = utils.yamls_in_dir(f'{root_dir}/configs', recursive=True)

  models_man.add_descriptors(yamls)

  entrypoint.start()

