import json
import time
import traceback
from datetime import datetime, timedelta
from functools import lru_cache
from json import JSONDecodeError
from typing import Optional, Dict, Tuple
from urllib.parse import quote

import requests
from k8kat.res.svc.kat_svc import KatSvc

from kama_sdk.core.core import utils
from kama_sdk.core.core.config_man import config_man
from kama_sdk.core.core.utils import pwar
from prom_kaml.main.types import PromData


class PromClient:
  _config: Optional[Dict]

  def __init__(self, config: Optional[Dict] = None):
    self._config = config

  def compute_vector(self, *args) -> Optional[PromData]:
    path, args = instant_path_and_args(*args)
    return self.do_invoke(path, args)

  def compute_matrix(self, *args) -> Optional[PromData]:
    path, args = gen_series_args(*args)
    return self.do_invoke(path, args)

  def do_invoke(self, path: str, url_args: Dict) -> Optional[PromData]:
    if self.is_prom_server_in_cluster():
      if svc := self.find_server_svc():
        if utils.is_in_cluster():
          base_url = self.get_base_in_cluster_url()
          response = invoke_normal_url(base_url, path, url_args)
        else:
          response = invoke_proxy_url(svc, path, url_args)
      else:
        return None
    else:
      base_url = self.get_base_out_of_cluster_url()
      response = invoke_normal_url(base_url, path, url_args)

    if response:
      return response.get('data')

  @lru_cache(maxsize=1)
  def find_server_svc(self) -> Optional[KatSvc]:
    if config := self.config():
      prom_ns = config.get(SVC_NS_KEY)
      prom_name = config.get(SVC_NAME_KEY)
      return KatSvc.find(prom_name, prom_ns)

  def config(self) -> Optional[Dict]:
    if self._config is None:
      root = config_man.manifest_variables(space='nmachine.prom')
      self._config = root
    return self._config

  def is_prom_server_in_cluster(self) -> bool:
    return self.config().get(ACCESS_TYPE_KEY) == access_type_k8s

  def get_base_in_cluster_url(self) -> str:
    if svc := self.find_server_svc():
      port = svc.first_tcp_port_num()
      return f"http://{svc.name}.{svc.namespace}:{port}"

  def get_base_out_of_cluster_url(self) -> str:
    return self.config().get(URL_KEY)


def instant_path_and_args(query: str, ts: datetime = None) -> Tuple:
  base = '/api/v1/query'
  ts = ts or datetime.now()
  args = {
    'query': query,
    'time': fmt_time(ts)
  }
  return base, args


def gen_series_args(query: str, step=None, t0=None, tn=None) -> Tuple:
  base = '/api/v1/query_range'
  t_start = t0 or datetime.now() - timedelta(days=7)
  t_end = tn or datetime.now()
  args = {
    'query': query,
    'start': fmt_time(t_start),
    'end': fmt_time(t_end),
    'step': step or '1h'
  }
  return base, args


def fmt_time(timestamp: datetime):
  return int(time.mktime(timestamp.timetuple()))


def invoke_proxy_url(svc: KatSvc, path: str, url_args: Dict) -> Optional[Dict]:
  resp = svc.proxy_get(path, url_args) or {}
  if resp.get('status', 500) < 300:
    try:
      body = resp.get('body')
      return body
    except:
      pwar(__name__, f"prom decode failed for resp {resp}", True)
      return None


def invoke_normal_url(base_url, path, args: Dict) -> Optional[Dict]:
  full_url = f"{base_url}{path}?{dict_args2str(args)}"
  resp = requests.get(full_url)
  if resp.ok:
    try:
      return resp.json()
    except JSONDecodeError:
      print(traceback.format_exc())
      print(resp)
      print(f"[kama_sdk:prom_client] svc resp decode ^^ fail")
      return None


def dict_args2str(args: Dict) -> str:
  as_list = [f"{k}={quote(str(v))}" for k, v in list(args.items())]
  return "&".join(as_list)


def invoke_pure_http(path, args) -> Optional[Dict]:
  arg2s = lambda arg: f"{arg[0]}={arg[1]}"
  url = f"{path}?{'&'.join(list(map(arg2s, args.items())))}"
  # noinspection PyBroadException
  try:
    return requests.get(url).json()
  except:
    print(traceback.format_exc())
    print(f"[kama_sdk:prom_client] pure http invoke ^^ fail")
    return None


prom_client = PromClient()

access_type_k8s = 'kubernetes'
access_type_generic = 'generic'

URL_KEY = 'url'
SVC_NS_KEY = 'service_namespace'
SVC_NAME_KEY = 'service_name'
ACCESS_TYPE_KEY = 'access_type'
