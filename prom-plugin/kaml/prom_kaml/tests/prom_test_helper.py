from k8kat.res.ns.kat_ns import KatNs

from kama_sdk.core.core.config_man import config_man
from kama_sdk.tests.t_helpers import helper
from prom_kaml.main import prom_client as client_module

def vanilla_setup():
  config_man.patch_user_vars({
    client_module.LOCATION_KEY: 'in',
    client_module.SVC_NS_KEY: svc_ns,
    client_module.SVC_NAME_KEY: svc_name
  }, space='nmachine.prom')


def easy_setup():
  if KatNs.find(svc_ns):
    helper.vanilla_setup()
    vanilla_setup()


svc_ns = 'monitoring'
svc_name = 'monitoring-kube-prometheus-prometheus'
