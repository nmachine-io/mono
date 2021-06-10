from typing import Optional

from k8kat.res.svc.kat_svc import KatSvc
from werkzeug.utils import cached_property

from kama_sdk.core.core import utils
from kama_sdk.core.telem import tabs_man
from kama_sdk.model.supplier.base.supplier import Supplier
from telem_kaml.telem_backend import TelemPluginBackend


class TelemStatusSupplier(Supplier):

  @cached_property
  def is_online(self):
    return client().is_enabled() and client().is_connected()

  @cached_property
  def is_enabled(self):
    return client().is_enabled()

  @cached_property
  def main_button_text(self):
    return "Disable / Migrate" if self.is_enabled else "Enable"

  @cached_property
  def main_button_action(self):
    enable_op = "nmachine.telem.operation.storage"
    disable_op = "nmachine.telem.operation.delete-telem-pvc"
    return disable_op if self.is_enabled else enable_op

  @cached_property
  def svc(self) -> Optional[KatSvc]:
    return client().get_svc()

  @cached_property
  def is_in_cluster(self):
    return utils.is_in_cluster()

  @cached_property
  def status(self):
    if client().is_enabled():
      if client().is_connected():
        return 'online'
      else:
        return 'offline'
    else:
      return 'disabled'

  @cached_property
  def action_preview_str(self):
    if self.is_online:
      if self.is_in_cluster:
        return "http://localhost"
      else:
        return client().collection_names()
    else:
      return 'no access'

  @cached_property
  def action_spec(self):
    if self.is_online:
      return dict(
        type='port_forward',
        uri=dict(
          pod_port=self.svc.first_tcp_port_num(),
          pod_name=self.svc.name,
          namespace=self.svc.namespace,
        )
      )




def client() -> TelemPluginBackend:
  # noinspection PyTypeChecker
  return tabs_man.get_backend()
