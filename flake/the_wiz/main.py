import os

import dotenv

from nectwiz.core.types import TamDict
from overrides import app_endpoints
from nectwiz import server
from nectwiz.core import utils
from nectwiz.core.wiz_app import wiz_app

root_dir = os.path.dirname(os.path.abspath(__file__))
yamls = utils.yamls_in_dir(f'{root_dir}/configs')

wiz_app.add_configs(yamls)
wiz_app.add_providers([app_endpoints.AppEndpointsProvider])

dotenv.load_dotenv()
server.start()
