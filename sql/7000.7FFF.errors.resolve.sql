SELECT parent.device_id, parent.host_rcpn, parent.device_type, json_agg(json_build_object('count', COALESCE(t.count,0))) as num_of_errors_in_window,
       'DEVICE_IN_ERROR_STATE' as alert_category,
        (NOW() - INTERVAL '12 hours') as transition_timestamp_utc
FROM alert_chunk.{table} AS parent
LEFT JOIN 
         ( SELECT device_id, count(device_id) as count
              FROM status.legacy_status_state_change lssc
              WHERE timestamp_utc >= NOW() - INTERVAL '12 hours'
              AND st BETWEEN x'7000'::int AND x'7FFF'::int
              GROUP BY lssc.device_id ) AS t
    ON t.device_id = parent.device_id
    AND t.count = 0
GROUP BY parent.device_id, parent.host_rcpn, parent.device_type, t.count;


