from moz.concerns.rbac_concern import RbacConcern
from moz.concerns.storage_concern import StorageConcern
from wiz.model.concern import Concern
from wiz.model.wizard import Wizard


class MosaicWizard(Wizard):

  @classmethod
  def concerns(cls) -> [Concern]:
    return [
      StorageConcern,
      RbacConcern
      # 'something'
    ]
