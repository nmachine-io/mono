from k8kat.res.ns.kat_ns import KatNs

from kama_sdk.tests.t_helpers import helper
from kama_sdk.tests.t_helpers.cluster_test import ClusterTest
from prom_kaml.main import prom_api_client


class TestPromApiClient(ClusterTest):

  def test_connection(self):
    if KatNs.find('monitoring'):
      helper.vanilla_setup()
      cli = prom_api_client
      svc = cli.find_prom_svc()
      self.assertTrue(cli.is_prom_server_in_cluster())
      self.assertTrue(cli.is_proxy())
      self.assertIsNotNone(svc)
      self.assertEqual('monitoring', svc.namespace)

  def test_invoke(self):
    if KatNs.find('monitoring'):
      helper.vanilla_setup()
      resp = prom_api_client.compute_vector('up')
      self.assertEqual('vector', resp['resultType'])
