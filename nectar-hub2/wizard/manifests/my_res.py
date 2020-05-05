from kubernetes.client import V1Deployment, V1ObjectMeta, V1DeploymentSpec, V1LabelSelector, V1PodTemplateSpec, \
  V1PodSpec, V1Container




def my_depl(**subs):
  default_labels = dict(app=subs['name'])
  labels = {**subs.get('labels', {}), **default_labels}
  match_labels = {**labels, **subs.get('selector', {})}

  return V1Deployment(
    metadata=V1ObjectMeta(
      name=subs['name'],
      labels=labels,
      annotations=subs.get('annotations', {})
    ),
    spec=V1DeploymentSpec(
      replicas=subs.get('replicas', 0),
      selector=V1LabelSelector(
        match_labels=match_labels
      ),
      template=V1PodTemplateSpec(
        metadata=V1ObjectMeta(labels=labels),
        spec=V1PodSpec(
          containers=[
            V1Container(
              name=subs.get("container", "primary"),
              image=subs.get('image', 'nginx'),
              image_pull_policy="IfNotPresent"
            )
          ]
        )
      )
    )
  )

