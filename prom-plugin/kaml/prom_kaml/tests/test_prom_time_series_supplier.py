from kama_sdk.model.humanizer.bytes_humanizer import BytesHumanizer
from kama_sdk.tests.t_helpers.cluster_test import ClusterTest
from prom_kaml.main.prom_matrix_to_timeseries_provider import PromMatrixToSeriesSupplier
from prom_kaml.main.types import PromMatrix


class TestPromMatrixToSeriesSupplier(ClusterTest):

  def test_convert_implicit_keys(self):
    actual = subject().matrix2series(prom_matrix_implicit_keys)
    self.assertEqual(expected_implicit, actual)

  def test_convert_explicit_keys(self):
    actual = subject().matrix2series(prom_matrix_explicit_keys)
    self.assertEqual(expected_explicit, actual)

  def test_with_humanizer(self):
    sup = subject(humanizer=f"kind::{BytesHumanizer.__name__}")
    actual = sup.matrix2series(prom_matrix_explicit_keys)
    print(actual)


def subject(**kwargs):
  return PromMatrixToSeriesSupplier(kwargs)


t0 = 1615803913

t1 = 1615807513

prom_matrix_implicit_keys: PromMatrix = [
  {
    "metric": {},
    'values': [[t0, "1"], [t1, "2"]]
  }
]

prom_matrix_explicit_keys: PromMatrix = [
  {
    "metric": {'foo': 'bar'},
    'values': [[t0, "1"], [t1, "2"]]
  },
  {
    "metric": {'foo': 'baz'},
    'values': [[t0, "3"], [t1, "4"]]
  },
  {
    "metric": {},
    'values': [[t0, "5"], [t1, "6"]]
  }
]


expected_implicit = [
  {'value': 1, 'timestamp': '2021-03-15 10:25:13'},
  {'value': 2, 'timestamp': '2021-03-15 11:25:13'}
]


expected_explicit = [
  {'bar': 1, 'baz': 3, 'value': 5, 'timestamp': '2021-03-15 10:25:13'},
  {'bar': 2, 'baz': 4, 'value': 6, 'timestamp': '2021-03-15 11:25:13'}
]
