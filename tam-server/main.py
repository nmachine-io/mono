import os
import subprocess

import yaml
from flask import Flask, jsonify

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get('SECRET_KEY')

executable = os.environ.get('TAMI_CMD', f'{os.getcwd()}/insane.sh')

@app.route('/values')
def values():
  print(executable)
  split_cmd = f"{executable} values".split(" ")
  yaml_out = subprocess.check_output(split_cmd, stderr=subprocess.STDOUT).decode('utf-8')
  as_dict = yaml.load(yaml_out)
  return jsonify(data=as_dict)


app.config["cmd"] = ["bash"]
app.run(host='0.0.0.0', port=5005, debug=True)
