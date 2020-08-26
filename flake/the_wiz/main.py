import os

import dotenv

from overrides import app_endpoints
from nectwiz import server
from nectwiz.core import utils
from nectwiz.core.wiz_app import wiz_app

root_dir = os.path.dirname(os.path.abspath(__file__))

wiz_app.add_configs(
  utils.yamls_in_dir(f'{root_dir}/configs')
)

wiz_app.add_providers([app_endpoints.AppEndpointsProvider])

wiz_app.app_name = 'flake'
wiz_app.tami_name = 'gcr.io/nectar-bazaar/flake-tami:latest'
wiz_app.tami_args = '-e hub-self-hosted'

dotenv.load_dotenv()
server.start()
