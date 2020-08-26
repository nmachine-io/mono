import dotenv

from overrides import app_endpoints
from wiz import server
from wiz.core import utils
from wiz.core.wiz_app import wiz_app

op_yamls_base = 'sample_wiz/operation-yamls'

wiz_app.add_configs(utils.yamls_in_dir('configs'))
wiz_app.add_providers([app_endpoints.AppEndpointsProvider])

wiz_app.app_name = 'flake'
wiz_app.tami_name = 'gcr.io/nectar-bazaar/flake-tami:latest'
wiz_app.tami_args = '-e hub-self-hosted'

dotenv.load_dotenv()
server.start()
