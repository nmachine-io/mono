from kama_sdk.model.predicate.predicate import Predicate
from kama_telem_plugin.models.telem_status_supplier import TelemStatusSupplier

class OnlineIfEnabledPredicate(Predicate):

  def resolve(self) -> bool:
    helper = TelemStatusSupplier({})
    if helper.is_enabled:
      return helper.is_online
    return True
