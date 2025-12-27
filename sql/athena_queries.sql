-- Total revenue by event date
SELECT
  DATE(event_ts) AS event_date,
  SUM(amount) AS total_revenue
FROM processed_events
WHERE event_type = 'purchase'
GROUP BY DATE(event_ts)
ORDER BY event_date;


-- Event counts by type
SELECT
  event_type,
  COUNT(*) AS event_count
FROM processed_events
GROUP BY event_type;

