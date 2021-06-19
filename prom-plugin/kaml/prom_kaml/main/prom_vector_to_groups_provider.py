from functools import lru_cache
from typing import Any, List

from kama_sdk.model.humanizer.quantity_humanizer import QuantityHumanizer

from kama_sdk.model.supplier.base.supplier import Supplier
from prom_kaml.main import prom_utils
from prom_kaml.main.types import PromVectorEntry


class PromVectorsToGroupsSupplier(Supplier):

  def source_data(self) -> List[PromVectorEntry]:
    return super(PromVectorsToGroupsSupplier, self).source_data()

  def _compute(self) -> Any:
    if data := self.source_data():
      grouped = self.vector2groups(data)
      return grouped
    else:
      return None

  @lru_cache
  def humanizer(self) -> QuantityHumanizer:
    return self.inflate_child(
      QuantityHumanizer,
      prop=HUMANIZER_KEY,
      lookback=False,
      safely=True
    )

  @lru_cache
  def with_unit(self) -> bool:
    return self.resolve_prop(APPEND_UNIT, lookback=False, backup=False)

  def vector2groups(self, vectors: List[PromVectorEntry]):
    result = []
    for i, vector in list(enumerate(vectors)):
      metric = vector.get('metric')
      value = vector.get('value')

      is_easy_label = isinstance(metric, dict) and len(metric) > 0
      is_easy_value = isinstance(value, list) and len(value) > 1

      metric_name = list(metric.values())[0] if is_easy_label else None
      num_value = value[1] if is_easy_value else None

      result.append({
        'name': metric_name or f"group {i + 1}",
        'value': prom_utils.process_num(
          num_value,
          self.humanizer(),
          self.with_unit()
        )
      })

    return result


HUMANIZER_KEY = 'humanizer'
APPEND_UNIT = 'with_unit'