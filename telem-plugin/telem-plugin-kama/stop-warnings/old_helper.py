# @model_attr(key='is_in_cluster', cached=True)
# def is_in_cluster(self):
#   return env_utils.is_in_cluster()

# @model_attr(key='is_online', cached=True)
# def action_preview_str(self):
#   if self.is_online:
#     if self.is_in_cluster:
#       return "http://localhost"
#     else:
#       return client().collection_names()
#   else:
#     return 'no access'

# @cached_property
# def action_spec(self):
#   if self.is_online:
#     return dict(
#       type='port_forward',
#       uri=dict(
#         pod_port=self.svc.first_tcp_port_num(),
#         pod_name=self.svc.name,
#         namespace=self.svc.namespace,
#       )
#     )
