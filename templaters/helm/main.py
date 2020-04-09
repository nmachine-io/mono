import subprocess
from pathlib import Path

import yaml
from typing import List, Dict


def mk_path(path):
  current = Path(__file__).resolve().parent
  return f"{current}{path}"

def outfile_path():
  return mk_path('output.yaml')

def manifests_path():
  return mk_path('/manifests')

def init_helm(repo_name):
  fqdn = f"https://github.com/{repo_name}"
  print(f"Running with {fqdn} -->  {manifests_path()}")
  subprocess.run(['git', 'clone', fqdn, manifests_path()])

def res_matches(res, identifier) -> bool:
  if res['kind'] == identifier['kind']:
    if res['metadata']['name'] == identifier['name']:
      return True
  return False

def ls():
  subprocess.run(['ls'])

def interpolate():
  command = f"helm template {manifests_path()}"
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
  f = open("tmp_res.yaml", "w")
  f.write(as_yaml)
  f.close()

def apply_res():
  subprocess.check_output(f"kubectl apply -f {outfile_path()}")
  subprocess.check_output(f"rm tmp_res.yaml")

fil = dict(kind='Secret', name='mysql')

res_defs = interpolate()
print(res_defs)
res_defs = filter_res(res_defs, [fil])
print(res_defs)
write_res(res_defs)
apply_res()

# def main():
#   if sys.argv[1] == 'init':
#     init_helm(sys.argv[2])
#   elif sys.argv[1] == 'ls':
#     print(manifests_path())
#   elif sys.argv[1] == 'interp':
#     print(interpolate())
#   elif sys.argv[1] == 'apply':
#    apply_interpolated()
#   elif sys.argv[1] == 'write':
#     write_interpolated(
#       filter_interpolated([
#         dict(kind='Pod', name='RELEASE-NAME-mysql-test')
#       ])
#     )
#   elif sys.argv[1] == 'filt':
#     print(filter_interpolated([
#       dict(kind='Pod', name='RELEASE-NAME-mysql-test')
#     ]))


# if __name__ == '__main__':
#   main()
#   sys.exit(0)
