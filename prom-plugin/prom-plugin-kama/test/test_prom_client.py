from k8kat.res.ns.kat_ns import KatNs

from kama_sdk.tests.t_helpers import helper
from kama_sdk.utils.unittest.base_classes import ClusterTest
from kama_prom_plugin.models.prom_client import prom_client
from test import prom_test_helper as my_helper


class TestPromClient(ClusterTest):

  def test_connection(self):
    if KatNs.find(my_helper.svc_ns):
      helper.vanilla_setup()
      my_helper.vanilla_setup()

      cli = prom_client
      svc = cli.find_prom_svc()
      self.assertIsNotNone(svc)
      self.assertEqual(my_helper.svc_ns, svc.namespace)
      self.assertEqual(my_helper.svc_name, svc.name)
      self.assertTrue(cli.is_prom_server_in_cluster())

  def test_invoke(self):
    if KatNs.find(my_helper.svc_ns):
      helper.vanilla_setup()
      my_helper.vanilla_setup()
      resp = prom_client.compute_vector('up')
      print(resp)
      self.assertEqual('vector', resp['resultType'])
