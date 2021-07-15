from kama_sdk.model.variable.manifest_variable_dependency import ManifestVariableDependency

def gen():
  pass


def gen_ingress_var_dep_descriptor(var_id: str):
  return {
    'kind': ManifestVariableDependency.__name__,
    'inherit': 'variable_dependency.template.ingress_disabled',
    'labels': {
      'from_variables': 'ingress.enabled',
      'to_variable': var_id
    }
  }

