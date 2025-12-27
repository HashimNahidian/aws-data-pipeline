-- This table is created automatically by the Glue Crawler
-- Shown here for reference and documentation purposes

CREATE EXTERNAL TABLE IF NOT EXISTS raw_events (
  event_id STRING,
  event_type STRING,
  user_id STRING,
  product_id STRING,
  amount DOUBLE,
  currency STRING,
  event_ts TIMESTAMP
)
ROW FORMAT SERDE 'org.openx.data.jsonserde.JsonSerDe'
LOCATION 's3://your-raw-bucket/events/';

