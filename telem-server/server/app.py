import base64
import json
import os
from typing import Optional, TypedDict, Dict

from bson import ObjectId
from flask import Flask, jsonify, request
from pymongo import MongoClient
from pymongo.database import Database
from pymongo.errors import ServerSelectionTimeoutError

import utils

app = Flask(__name__)

class Memory(TypedDict):
  status: str
  database: Optional[Database]


memory: Memory = {
  'status': 'idle',
  'database': None
}


@app.route('/collections/<collection_id>/query')
def query_collection(collection_id: str):
  if prep_state():
    query = args_query2dict()
    collection = database()[collection_id]
    records = list(collection.find(query))
    return jsonify(data=list(map(serialize_record, records)))
  else:
    return respond_not_connected_400()


@app.route('/collections/<collection_id>/find/<record_id>')
def find_record_by_id(collection_id, record_id):
  if prep_state():
    if record := find_record(collection_id, {'_id': ObjectId(record_id)}):
      return jsonify(data=serialize_record(record))
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
  connection_params = gen_connection_params()
  try:
    client = MongoClient(
      **connection_params,
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


def gen_connection_params():
  if is_auto_pvc():
    return dict(
      host='localhost',
      port=27017
    )
  else:
    return dict(
      host=os.environ.get(host_key),
      port=os.environ.get(port_key)
    )


def is_auto_pvc() -> bool:
  if strategy := get_hosting_strategy():
    return strategy == 'managed_pvc'
  else:
    return True


def get_hosting_strategy():
  return os.environ.get('STRATEGY')


def serialize_record(record: Dict) -> Dict:
  new_record = {}
  for key, value in record.items():
    if isinstance(value, ObjectId):
      new_record[key] = str(value)
    else:
      new_record[key] = value
  return new_record


if __name__ == '__main__':
  app.run()


host_key = 'HOST'
port_key = 'PORT'
