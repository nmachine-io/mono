from k8kat.res.ns.kat_ns import KatNs
from kama_sdk.tests.t_helpers import helper
from prom_kaml.tests import prom_test_helper as my_helper

from kama_sdk.tests.t_helpers.cluster_test import ClusterTest
from prom_kaml.main.prom_data_supplier import PromDataSupplier
from prom_kaml.main import prom_data_supplier as supplier_module


class TestPromDataSupplier(ClusterTest):

  def test_resolve_default_client_config(self):
    if my_helper.easy_setup():
      supplier = PromDataSupplier.inflate({
        supplier_module.TYPE_KEY: 'vector'
      })
      self.assertTrue(supplier.resolve())

  def test_resolve_custom_client_config(self):
    if my_helper.easy_setup():
      helper.vanilla_setup()
      my_helper.vanilla_setup()

    supplier = PromDataSupplier.inflate({
      supplier_module.TYPE_KEY: 'ping',
      supplier_module.CLIENT_CONFIG: {}
    })
    self.assertTrue(supplier.resolve())
