from k8_kat.res.pvc.kat_pvc import KatPvc
from moz.mosaic_concern import MosaicConcern
from wiz.model.part import Part


class SetPvcNamePart(Part):

  def list_pvcs(self):
    KatPvc.q()


class StorageConcern(MosaicConcern):

  def __init__(self):
    pass

  def next_step(self, crt_step):
    if crt_step == '':
      pass


