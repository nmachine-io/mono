from typing import Optional

from k8kat.res.svc.kat_svc import KatSvc

from kama_sdk.core.telem.telem_manager import telem_manager
from kama_sdk.model.base.model import Model
from kama_sdk.model.base.model_decorators import model_attr
from kama_sdk.utils import env_utils
from kama_telem_plugin.nmachine_telem_backend import NMachineTelemBackend


class TelemStateHelper(Model):

  @model_attr(key='is_online', cached=True)
  def is_online(self):
    return client().is_enabled() and client().is_connected()

  @model_attr(key='is_offline', cached=True)
  def is_offline(self):
    return client().is_enabled() and client().is_connected()

  @model_attr(key='is_enabled', cached=True)
  def is_enabled(self):
    return client().is_enabled()

  @model_attr(key='is_disabled', cached=True)
  def is_disabled(self):
    return not self.is_enabled()

  # @cached_property
  # def main_button_action(self):
  #   enable_op = "nmachine.telem.operation.storage"
  #   disable_op = "nmachine.telem.operation.delete-telem-pvc"
  #   return disable_op if self.is_enabled else enable_op

  @model_attr(key='svc', cached=True)
  def svc(self) -> Optional[KatSvc]:
    return client().get_svc()

  @model_attr(key='is_in_cluster', cached=True)
  def is_in_cluster(self):
    return env_utils.is_in_cluster()

  @model_attr(key='status', cached=True)
  def status(self):
    if client().is_enabled():
      if client().is_connected():
        return 'online'
      else:
        return 'offline'
    else:
      return 'disabled'

  # @model_attr(key='is_online', cached=True)
  # def action_preview_str(self):
  #   if self.is_online:
  #     if self.is_in_cluster:
  #       return "http://localhost"
  #     else:
  #       return client().collection_names()
  #   else:
  #     return 'no access'

  # @cached_property
  # def action_spec(self):
  #   if self.is_online:
  #     return dict(
  #       type='port_forward',
  #       uri=dict(
  #         pod_port=self.svc.first_tcp_port_num(),
  #         pod_name=self.svc.name,
  #         namespace=self.svc.namespace,
  #       )
  #     )


def client() -> Optional[NMachineTelemBackend]:
  backend = telem_manager.get_backend()
  is_from_this_plugin = isinstance(backend, NMachineTelemBackend)
  return backend if is_from_this_plugin else None
