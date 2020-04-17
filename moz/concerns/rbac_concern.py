from moz.concerns.mosaic_concern import MosaicConcern


class RbacConcern(MosaicConcern):

  @classmethod
  def name(cls):
    return "Persistent Storage Setup"
