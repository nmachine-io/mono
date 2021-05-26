import json
import os
from typing import Any

from flask import request


def parse_json_body():
  try:
    return unmuck_primitives(request.json)
  except Exception:
    payload_str = request.data.decode('unicode-escape')
    print("ORIGINAL PAYLOAD")
    print(payload_str)
    truncated = payload_str[1:len(payload_str) - 1]
    print("TRUNCED")
    print(print(payload_str))
    as_dict = json.loads(truncated)
    print("PARSED")
    print(json.loads(truncated))
    return unmuck_primitives(as_dict)


def isfloat(value):
  try:
    float(value)
    return True
  except ValueError:
    return False


def unmuck_primitive(original: Any) -> Any:
  if type(original) == str:
    if original.isdigit():
      return int(original)
    elif isfloat(original):
      return float(original)
    elif original.lower() == 'true':
      return True
    elif original.lower() == 'false':
      return False
    else:
      return original
  else:
    return original


def run_env() -> str:
  return os.environ.get('FLASK_ENV', 'production')


def is_production():
  return run_env() == 'production'


def unmuck_primitives(root: Any) -> Any:
  if type(root) == dict:
    return {k: unmuck_primitives(v) for k, v in root.items()}
  elif type(root) == list:
    return list(map(unmuck_primitives, root))
  else:
    return unmuck_primitive(root)
