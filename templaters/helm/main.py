import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

import yaml
from typing import List, Dict

def mk_path(path):
  current = Path(__file__).resolve().parent
  return f"{current}{path}"

def outfile_path():
  return mk_path('/output.yaml')

def cloned_helm_path():
  return mk_path('/helm_res')

def overrides_path():
  return f"{cloned_helm_path()}/overrides.yaml"

def values_path():
  return f"{cloned_helm_path()}/values.yaml"

def deep_merge(source, destination):
  for key, value in source.items():
    if isinstance(value, dict):
      node = destination.setdefault(key, {})
      deep_merge(value, node)
    else:
      destination[key] = value
    return destination

def init_helm(repo_name):
  fqdn = f"https://github.com/{repo_name}"
  if os.path.exists(cloned_helm_path()):
    print(f"Warn: force deleting {cloned_helm_path()}")
    shutil.rmtree(cloned_helm_path())
  clone_cmd = f"git clone {fqdn} {cloned_helm_path()}"
  subprocess.check_output(clone_cmd, shell=True)

def res_matches(res, identifier) -> bool:
  if res['kind'] == identifier['kind']:
    if res['metadata']['name'] == identifier['name']:
      return True
  return False

def interpolate():
  f_paths = " -f ".join([values_path(), overrides_path()])
  command = f"helm template {cloned_helm_path()} -f {f_paths}"
  output = subprocess.check_output(command, shell=True)
  output = output.decode('utf-8').replace('RELEASE-NAME-', '')
  res_iterator = yaml.load_all(output, yaml.FullLoader)
  return [res for res in res_iterator]

def filter_res(res_defs, identifiers: List[Dict[str, str]]) -> List[Dict]:
  targets = []
  for res in res_defs:
    for identifier in identifiers:
      if res_matches(res, identifier):
        targets.append(res)
        break
  return targets

def write_res(res_defs: List[Dict]):
  as_yaml = yaml.dump_all(res_defs)
  f = open(outfile_path(), "w")
  f.write(as_yaml)
  f.close()

def read_override_values():
  path = os.environ.get(
    'NECTAR_VALUES_PATH',
    mk_path('/dummy_config')
  )
  return json.loads(open(path, 'r').read())

def create_overrides_yaml():
  file = open(overrides_path(), "w")
  file.write(yaml.dump(read_override_values()))
  file.close()

def apply_res():
  apply_cmd = f"kubectl apply -f {outfile_path()}"
  subprocess.check_output(apply_cmd, shell=True)
  # subprocess.check_output(f"rm {outfile_path()}", shell=True)

def parse_ids(ser_ids):
  to_dict = lambda x: dict(kind=x[0], name=x[1])
  return [to_dict(pair.split(':')) for pair in ser_ids]

def filter_only(ser_ids):
  create_overrides_yaml()
  res_defs = interpolate()
  return filter_res(res_defs, ser_ids)

def apply(ser_ids):
  res_defs = filter_only(ser_ids)
  write_res(res_defs)
  apply_res()

def main():
  if len(sys.argv) < 1:
    print("Need 1 arg")
  elif sys.argv[1] == 'init':
    init_helm(sys.argv[2])
  elif sys.argv[1] == 'ls':
    print(cloned_helm_path())
  elif sys.argv[1] == 'interpolate':
    print(interpolate())
  elif sys.argv[1] == 'overrides':
    print(read_override_values())
  elif sys.argv[1] == 'override':
    create_overrides_yaml()
  elif sys.argv[1] == 'filter':
    print(filter_only(parse_ids(sys.argv[2:])))
  elif sys.argv[1] == 'apply':
    apply(parse_ids(sys.argv[2:]))


if __name__ == '__main__':
  main()
  sys.exit(0)
