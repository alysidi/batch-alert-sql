from . import config
from psycopg2 import pool
from proto import stormprep_pb2
import pytest
import pandas as pd
import json

@pytest.fixture
def db():
    postgres_pool = pool.SimpleConnectionPool(1, 5, **config.TIMESCALE_STAGE_REPLICA_DB_CONNECTION)
    conn = postgres_pool.getconn()
    conn.set_session(autocommit=True)
    return conn


def test_error_raise_query(db):


  with open('../sql/7000.7FFF.errors.raise.sql', 'r') as file:
    sql_query = file.read()
    context = '000100071F39'
    df = pd.read_sql_query(sql_query.format(context), db)
    result = json.loads(df.to_json(orient='records'))
  assert( context== result[0]['device_id'] )