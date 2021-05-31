import json
import time
import traceback
from datetime import datetime, timedelta
from json import JSONDecodeError
from typing import Optional, Dict, Tuple
from urllib.parse import quote

import requests
from k8kat.res.svc.kat_svc import KatSvc

from kama_sdk.core.core import utils
from kama_sdk.core.core.config_man import config_man
from prom_kaml.main.types import PromData


def compute_vector(*args) -> Optional[PromData]:
  path, args = instant_path_and_args(*args)
  return do_invoke(path, args)


def compute_matrix(*args) -> Optional[PromData]:
  path, args = gen_series_args(*args)
  # print("PATH")
  # print(path)
  # print(args)
  return do_invoke(path, args)


def do_invoke(path: str, url_args: Dict) -> Optional[PromData]:
  if is_prom_server_in_cluster():
    if svc := find_prom_svc():
      if utils.is_in_cluster():
        response = invoke_url(path, url_args)
      else:
        response = invoke_svc(svc, path, url_args)
    else:
      return None
  else:
    response = invoke_url(path, url_args)

  if response:
    return response.get('data')


def invoke_url(path, args: Dict) -> Optional[Dict]:
  base_url = prom_config().get(URL_KEY)
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


def invoke_svc(svc: KatSvc, path: str, url_args: Dict) -> Optional[Dict]:
  resp = svc.proxy_get(path, url_args) or {}
  # print(path)
  # print(url_args)
  if resp.get('status', 500) < 300:
    try:
      return json.loads(resp.get('body'))
    except JSONDecodeError:
      print(traceback.format_exc())
      print(resp.get('body'))
      print(f"[kama_sdk:prom_client] svc resp decode ^^ fail")
      return None


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


def find_prom_svc() -> Optional[KatSvc]:
  if not _cache_obj[CACHE_SVC_KEY]:
    prefs = prom_config()
    prom_ns = prefs.get(SVC_NS_KEY)
    prom_name = prefs.get(SVC_NAME_KEY)
    _cache_obj[CACHE_SVC_KEY] = KatSvc.find(prom_name, prom_ns)
    if not _cache_obj['svc']:
      print(f"[kama_sdk:prom_client] svc [{prefs}] not found")
  return _cache_obj[CACHE_SVC_KEY]


def prom_config() -> Dict:
  if not _cache_obj[CACHE_CONFIG_KEY]:
    root = config_man.prefs().get('monitoring') or {}
    _cache_obj[CACHE_CONFIG_KEY] = root
  return _cache_obj[CACHE_CONFIG_KEY] or {}


def is_prom_server_in_cluster() -> bool:
  return prom_config().get(LOCATION_KEY, 'out') == 'in'


URL_KEY = 'url'
SVC_NS_KEY = 'service_namespace'
SVC_NAME_KEY = 'service_name'

CACHE_CONFIG_KEY = 'prom_config'
CACHE_SVC_KEY = 'svc'
LOCATION_KEY = 'relative_to_cluster'

_cache_obj = {
  CACHE_CONFIG_KEY: {},
  CACHE_SVC_KEY: None
}