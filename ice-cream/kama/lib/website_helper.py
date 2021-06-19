from typing import Optional

from k8kat.res.svc.kat_svc import KatSvc
from kama_sdk.model.concern.concern import Concern

from kama_sdk.model.base.model_decorators import model_attr
from kama_sdk.model.supplier.ext.misc.port_forward_spec_supplier import PortForwardSpecSupplier

from kama_sdk.core.core.types import PortForwardSpec

from kama_sdk.core.core.config_man import config_man

from lib import consts


class WebsiteHelper(Concern):

  @model_attr(cache=True)
  def svc(self) -> Optional[KatSvc]:
    return KatSvc.find(consts.workload_name, config_man.ns())

  @model_attr(cache=True)
  def is_online(self) -> bool:
    if svc := self.svc():
      return len(svc.endpoint_ips) > 0
    else:
      return False

  @model_attr()
  def status(self):
    return "Online" if self.is_online() else "Offline"

  @model_attr()
  def port_forward_spec(self) -> Optional[PortForwardSpec]:
    return PortForwardSpecSupplier({'source': self.svc}).resolve()
