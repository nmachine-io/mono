from typing import List

from k8kat.res.ingress.kat_ingress import KatIngress
from k8kat.res.svc.kat_svc import KatSvc

from nectwiz.core.core.config_man import config_man
from nectwiz.model.adapters.app_endpoint_adapter import AppEndpointAdapter
from nectwiz.model.adapters.provider import Provider


class HomepageAdapter(AppEndpointAdapter):
  def name(self):
    return "Homepage"

  def url(self):
    ingress = KatIngress.find('hub-ingress', config_man.ns())
    host, host_info = list(ingress.basic_rules().items())[0]
    info = [b for b in host_info if b['service'] == 'hub-front'][0]
    path = '' if info['path'] == '/' else info['path']
    return f"{host}{path}"


class HomepageInternalAdapter(AppEndpointAdapter):
  def name(self):
    return "Homepage internal"

  def url(self):
    svc = KatSvc.find('hub-front', config_man.ns())
    return f"{svc.internal_ip}:{svc.from_port}"


class AdminPageAdapter(HomepageAdapter):
  def name(self):
    return "Admin Panel"

  def url(self):
    return f"{super().url()}/admin"


class AppEndpointsProvider(Provider[AppEndpointAdapter]):

  @classmethod
  def kind(cls):
    return AppEndpointAdapter

  def produce_adapters(self) -> List[AppEndpointAdapter]:
    return [
      HomepageAdapter(),
      HomepageInternalAdapter(),
      AdminPageAdapter()
    ]
