from k8_kat.auth.kube_broker import broker
from wiz.core import core, utils
from wiz.core.base_adapter import PythonBackend

if __name__ == '__main__':
  broker.connect()
