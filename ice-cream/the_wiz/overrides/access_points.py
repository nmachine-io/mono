from typing import List, Optional

from k8kat.res.pod.kat_pod import KatPod
from k8kat.res.svc.kat_svc import KatSvc

from nectwiz.core.core.config_man import config_man
from nectwiz.model.adapters.app_endpoints_adapter import AccessPointsAdapter, AccessPointDict


class IceCreamAccessPoints(AccessPointsAdapter):

  def access_points(self) -> List[AccessPointDict]:
    return [
      homepage_ap(),
      admin_console_ap()
    ]


def homepage_ap() -> Optional[AccessPointDict]:
  svc = KatSvc.find('ice-cream', config_man.ns())
  if svc:
    return AccessPointDict(
      name='Homepage',
      url=f"{svc.internal_ip}:{svc.from_port}",
      type='internal-url'
    )


def admin_console_ap() -> Optional[AccessPointDict]:
  pods = KatPod.list(config_man.ns(), labels={'app': 'ice-cream'})
  pod = next(filter(KatPod.is_running, pods), None)
  if pod:
    return AccessPointDict(
      name='Admin Console',
      resource=dict(kind='pod', name=pod.name),
      command='bundle exec rails console',
      type='command'
    )
