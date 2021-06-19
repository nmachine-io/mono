import os
from typing import List, Dict, Type

from kama_sdk.core.core.kaml import KamlDescriptor
from kama_sdk.core.core import utils
from kama_sdk.model.base.model import Model
from prom_kaml.main.grafana_state_supplier import GrafanaStateSupplier
from prom_kaml.main.prom_data_supplier import PromDataSupplier
from prom_kaml.main.prom_matrix_to_timeseries_supplier import PromMatrixToSeriesSupplier
from prom_kaml.main.prom_state_supplier import PromStateSupplier
from prom_kaml.main.prom_vector_to_groups_provider import PromVectorsToGroupsSupplier


def describe_self():
  return KamlDescriptor(
    id='nmachine.prom',
    publisher_identifier='nmachine',
    app_identifier='prom-plugin',
    model_classes=model_classes(),
    asset_paths=[assets_path],
    model_descriptors=model_descriptors(),
  )


def model_classes() -> List[Type[Model]]:
  return [
    PromDataSupplier,
    PromMatrixToSeriesSupplier,
    PromVectorsToGroupsSupplier,
    PromStateSupplier,
    GrafanaStateSupplier
  ]


def model_descriptors() -> List[Dict]:
  return utils.yamls_in_dir(yamls_path, recursive=True)


root_dir = os.path.dirname(os.path.abspath(__file__))
yamls_path = f'{root_dir}/yamls'
assets_path = f'{root_dir}/assets'
