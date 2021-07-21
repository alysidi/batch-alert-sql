
import os 

TIMESCALE_STAGE_REPLICA_DB_CONNECTION = {
   "user":os.environ.get('TS_STG_USERNAME'),
   "password":os.environ.get('TS_STG_PASSWORD'), 
   "host":"timescaledb-stg.neur.io",
   "port":"12949",
   "database":"defaultdb"
}