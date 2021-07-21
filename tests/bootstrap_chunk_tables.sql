-- Run this file on Timescale STG to refresh the data if the tests fail


-- Used in 7000.7FFF.errors.raise.sql
drop table alert_chunk.errors_raise_7000;

select * into alert_chunk.errors_raise_7000 from status.device_shadow
where timestamp_utc > now() - interval '1 month' and st = x'7000'::int
order by timestamp_utc desc limit 10;

select * from alert_chunk.errors_raise_7000;


-- User in 7000.7FFF.errors.resolve.sql
drop table alert_chunk.errors_resolve_7000;

select * into alert_chunk.errors_resolve_7000 from status.device_shadow
where timestamp_utc > now() - interval '0 day'
order by timestamp_utc desc limit 10;

select * from alert_chunk.errors_resolve_7000;
