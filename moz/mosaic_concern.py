import os

from wiz.model.concern import Concern


class MosaicConcern(Concern):

  @classmethod
  def defaults_fname(cls):
    full_path = os.path.realpath(__file__)
    path, filename = os.path.split(full_path)
    return f"{path}/constants.yaml"

