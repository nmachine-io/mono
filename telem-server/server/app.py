import base64
import json
import os
from typing import Optional, TypedDict, Dict

from bson import ObjectId
from flask import Flask, jsonify, request
from flask_cors import CORS
from pymongo import MongoClient
from pymongo.database import Database
from pymongo.errors import ServerSelectionTimeoutError

import utils


host_key = 'DB_HOST'
port_key = 'DB_PORT'
own_port_key = 'PORT'


app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get('SECRET_KEY')
CORS(app)


class Memory(TypedDict):
  status: str
  database: Optional[Database]


memory: Memory = {
  'status': 'idle',
  'database': None
}


@app.route('/')
def home():
  return jsonify(data=dict(app='telem'))


@app.route('/collections/index')
def list_collection():
  if prep_state():
    names = database().list_collection_names()
    return jsonify(data=names)
  else:
    return respond_not_connected_400()


@app.route('/collections/<collection_id>/drop', methods=['POST'])
def drop_collection(collection_id: str):
  if prep_state():
    query = args_query2dict()
    database()[collection_id].drop()
    return jsonify(status='success')
  else:
    return respond_not_connected_400()



@app.route('/collections/<collection_id>/query')
def query_collection(collection_id: str):
  if prep_state():
    query = args_query2dict()
    collection = database()[collection_id]
    records = list(collection.find(query))
    return jsonify(data=list(map(serialize_for_serving, records)))
  else:
    return respond_not_connected_400()


@app.route('/collections/<collection_id>/find/<record_id>')
def find_record_by_id(collection_id, record_id):
  if prep_state():
    if record := find_record(collection_id, {'_id': ObjectId(record_id)}):
      return jsonify(data=serialize_for_serving(record))
    else:
      error = f"record {collection_id}/{record_id} not found"
      return jsonify(error=error), 404
  else:
    return respond_not_connected_400()


@app.route('/collections/<collection_id>/insert', methods=['POST'])
def insert_into_collection(collection_id: str):
  if prep_state():
    data = utils.parse_json_body()['data']
    collection = database()[collection_id]
    collection.insert_one(data)
    return jsonify(status='success')
  else:
    return respond_not_connected_400()


def find_record(collection_id: str, query: Dict):
  collection = database()[collection_id]
  return collection.find_one(query)


def respond_not_connected_400():
  return jsonify(error='db not connected'), 400


def prep_state() -> Optional[Database]:
  if memory['status'] == 'idle':
    db = connect()
    memory['database'] = db
    memory['status'] = 'connected' if db else 'error'
  return memory['database'] if memory['status'] == 'connected' else None


def database() -> Optional[Database]:
  return memory['database']


def connect() -> Optional[Database]:
  try:
    client = MongoClient(
      host=os.environ.get(host_key),
      port=int(os.environ.get(port_key)),
      connectTimeoutMS=1_000,
      serverSelectionTimeoutMS=1_000
    )
    client.server_info()
    return client['database']

  except ServerSelectionTimeoutError:
    return None

def args_query2dict() -> Dict:
  if b64_json_encoded := request.args.get('query'):
    json_encoded_utf_reconstructor = base64.b64decode(b64_json_encoded)
    return json.loads(json_encoded_utf_reconstructor)
  else:
    return {}


def serialize_for_serving(record: Dict) -> Dict:
  new_record = {}
  for key, value in record.items():
    if isinstance(value, ObjectId):
      new_record[key] = str(value)
    else:
      new_record[key] = value
  return new_record


def ser_for_storage(record: Dict):
  new_record = {}
  for key, value in record.items():
    if isinstance(value, dict):
      new_record[key] = json.dumps(value)
    else:
      new_record[key] = value
  return new_record


if __name__ == '__main__':
  own_port = int(os.environ.get(own_port_key, '5000'))
  app.run(host='0.0.0.0', port=own_port)
