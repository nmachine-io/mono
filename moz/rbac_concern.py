from moz.mosaic_concern import MosaicConcern
from wiz.model.concern import Concern


class RbacConcern(MosaicConcern):

  @classmethod
  def name(cls):
    return "Persistent Storage Setup"
