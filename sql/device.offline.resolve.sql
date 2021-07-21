
SELECT parent.device_id, parent.host_rcpn, parent.device_type, json_agg(json_build_object('count', 0)) as num_of_errors_in_window,
       'DEVICE_OFFLINE' as alert_category,
       t.transition_timestamp_utc 
FROM alert_chunk.{table} AS parent
JOIN 
         (    SELECT device_id, 
              timestamp_utc as transition_timestamp_utc
              FROM status.device_shadow ds
              LEFT JOIN status.rcp_state r ON r.state_code = (ds.st & x'FFF0'::int)
              WHERE timestamp_utc >= now() - INTERVAL '10 minutes'
              GROUP BY device_id, timestamp_utc ) AS t
    ON t.device_id = parent.device_id
GROUP BY parent.device_id, parent.host_rcpn, parent.device_type,  t.transition_timestamp_utc;





