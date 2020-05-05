import moz
from k8_kat.auth.kube_broker import broker
from moz import concerns
from wiz.core import core, utils
from wiz.core.base_adapter import PythonBackend
from wiz.model.concern import Concern

if __name__ == '__main__':
  broker.connect()
