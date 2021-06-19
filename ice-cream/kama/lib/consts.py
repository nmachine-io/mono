from kama_sdk.model.base.model_decorators import model_attr
from kama_sdk.model.supplier.base.supplier import Supplier

workload_name = 'ice-cream'
site_logo = "https://freeiconshop.com/wp-content/uploads/edd/ice-cream-cone-outline-filled.png"

class IceCreamConsts(Supplier):

  @model_attr()
  def workload_name(self):
    return workload_name

  @model_attr()
  def site_logo(self):
    return site_logo
