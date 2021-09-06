from typing import List, Dict

from kama_sdk.core.ktea.ktea_client import KteaClient

from kama_sdk.core.ktea.ktea_provider import ktea_client
from kama_sdk.core.ktea.virtual_ktea_client import VirtualKteaClient
from kama_sdk.utils.utils import deep_set


class V2VirtualKtea(VirtualKteaClient):

  def _default_values(self) -> Dict:
    return backing_client().load_default_values()

  def _template(self, values: Dict) -> List[Dict]:
    res_descs = backing_client().template_manifest(values)
    if isinstance(res_descs, list):
      for res_desc in res_descs:
        if isinstance(res_desc, dict):
          deep_set(res_desc, "metadata.annotations.version", "2.0.0")
    return res_descs


def backing_client() -> KteaClient:
  return ktea_client(ktea=BACKING_KTEA_DICT)


BACKING_KTEA_DICT = {
  'type': 'server',
  'uri': 'https://api.nmachine.io/ktea/nmachine/ice-kream-ktea',
  'version': '1.0.1'
}
