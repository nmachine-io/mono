from typing import Dict
import yaml
from wiz import server

from wiz.core.wiz_globals import wiz_globals

def load_yaml_array(fname) -> [Dict]:
  file_contents = open(fname, 'r').read()
  return yaml.load(file_contents, Loader=yaml.FullLoader)['data']

wiz_globals.set_configs(
  concerns=load_yaml_array('wizard/constants/concerns.yaml'),
  steps=load_yaml_array('wizard/constants/steps.yaml'),
  fields=load_yaml_array('wizard/constants/fields.yaml'),
)

server.start()
