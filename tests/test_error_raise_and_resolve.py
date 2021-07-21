from . import config
from psycopg2 import pool
import pytest
import pandas as pd
import json
from proto import alertDetectionEvent_pb2 as alert_detection
from google.protobuf.json_format import MessageToJson
from google.protobuf import json_format

@pytest.fixture
def db():
    postgres_pool = pool.SimpleConnectionPool(1, 5, **config.TIMESCALE_STAGE_REPLICA_DB_CONNECTION)
    conn = postgres_pool.getconn()
    conn.set_session(autocommit=True)
    return conn

def dataframe_to_proto(df):
    result = json.loads(df.to_json(orient='records'))
    return json_format.Parse(json.dumps(result[0]), alert_detection.AlertDetectionEvent(), ignore_unknown_fields=False)


def test_7000_7FFF_errors_raise_query(db):
  with open('../sql/7000.7FFF.errors.raise.sql', 'r') as file:
    sql_query = file.read()
    context = {'table':'errors_raise_7000'}

    df = pd.read_sql_query(sql_query.format(**context), db)
    alert_detection_proto = dataframe_to_proto(df)

  assert( alert_detection_proto.device_id != '' )
  assert( alert_detection_proto.num_of_errors_in_window[0].error_device_state != '' )
  

def test_7000_7FFF_errors_resolve_query(db):
  with open('../sql/7000.7FFF.errors.resolve.sql', 'r') as file:
    sql_query = file.read()
    context = {'table':'errors_resolve_7000'}

    df = pd.read_sql_query(sql_query.format(**context), db)
    alert_detection_proto = dataframe_to_proto(df)

  assert( alert_detection_proto.device_id != '' )
  assert( alert_detection_proto.num_of_errors_in_window[0].count == 0 )



