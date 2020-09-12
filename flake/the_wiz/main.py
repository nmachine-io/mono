import os

from nectwiz import entrypoint
from nectwiz.model.base.wiz_model import models_man
from overrides import app_endpoints
from nectwiz.core.core import utils

if __name__ == '__main__':
  root_dir = os.path.dirname(os.path.abspath(__file__))
  yamls = utils.yamls_in_dir(f'{root_dir}/configs')

  models_man.add_descriptors(yamls)
  models_man.add_classes([app_endpoints.AppEndpointsProvider])

  entrypoint.start()
