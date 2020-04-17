from k8_kat.res.base.k8_kat import K8Kat
from k8_kat.res.pvc.kat_pvc import KatPvc
from moz.concerns.mosaic_concern import MosaicConcern
from wiz.model.part import Part
from wiz.model.step import Step


class SetPvcNamePart(Part):
  def list_pvcs(self):
    KatPvc.q()

class SetPvcNameStep(Step):

  def commit(self):
    pass

class Secrets(Step):
  pass

class Host(Part):

  def res(self):
    return [
      K8Kat.svcs().ns(self.ns).find(self.config.name)
    ]

class CreateVolumeStep(Step):

  def next_step(self, context):
    if context['create_volume']:
      return "database_secrets"
    else:
      return "locate_volume"

class StorageConcern(MosaicConcern):

  @classmethod
  def step(cls, name) -> Step:
    pass

  def __init__(self):
    pass

  def next_step(self, crt_step):
    if crt_step == '':
      pass


