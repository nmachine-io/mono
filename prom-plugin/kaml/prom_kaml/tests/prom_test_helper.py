from k8kat.res.ns.kat_ns import KatNs

from kama_sdk.core.core.config_man import config_man
from kama_sdk.model.base.model import models_man
from kama_sdk.tests.t_helpers import helper
from prom_kaml import kaml
from prom_kaml.main import prom_client as client_module
from prom_kaml.main import prom_data_supplier as supplier_module
from prom_kaml.main.prom_data_supplier import PromDataSupplier


def vanilla_setup():
  config_man.patch_user_vars({
    client_module.ACCESS_TYPE_KEY: client_module.access_type_k8s,
    client_module.SVC_NS_KEY: svc_ns,
    client_module.SVC_NAME_KEY: svc_name
  }, space='nmachine.prom')


def vanilla_matrix_supplier():
  return PromDataSupplier.inflate({
    'kind': PromDataSupplier.__name__,
    supplier_module.TYPE_KEY: 'matrix',
    supplier_module.STEP_KEY: '15m',
    'source': "container_memory_usage_bytes{namespace=\"monitoring\"}"
  })


def easy_setup() -> bool:
  if KatNs.find(svc_ns):
    helper.vanilla_setup()
    vanilla_setup()
    models_man.add_classes(kaml.model_classes())
    models_man.add_descriptors(kaml.model_descriptors())
    return True
  else:
    return False


svc_ns = 'monitoring'
svc_name = 'monitoring-kube-prometheus-prometheus'
