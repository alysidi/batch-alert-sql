## How the Batch SQL Tests Work

All queries are stored in the `sql` folder. Each test will execute a templated SQL, and convert the result to JSON.
The JSON will then be parsed into the alert detection event protobuf. This is to ensure the output of the SQL matches the 
proto schema. The Alert Detect Service ( ADS ) will use this protobuf as a contract, so any changes to the SQL must conform.

## Types of SQL queries

### `raise` -> detects alerts
Has the full proto sent that will be enriched by ADS

### `resolve` -> resolves alerts
The `num_of_errors_in_window` field will contain the result of `[{"count":0}]` which let's the ADS know that there are no errors within a given hop window.


## Script to Run

`./run_batch_tests_sql.sh` will pull the latest blitz repo, compile the alert detection protobuf and put it into the `proto` folder in the root. It will then run the pytest. This file needs to be run from the root folder. If you run pytest manually, run it from within the `tests` folder.

`tests/bootstrap.sql` will populate the chunk tables needed to run the scripts

## Credentials

Ensure your ENV variables are set for connecting to the Timescale Stage Replica DB

````
"user":os.environ.get('TS_STG_USERNAME')
"password":os.environ.get('TS_STG_PASSWORD')
```
