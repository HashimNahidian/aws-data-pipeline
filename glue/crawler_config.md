# Glue Crawler Configuration

## Purpose
Automatically discover schema from raw JSON files stored in S3 and create tables in the Glue Data Catalog.

## Configuration
- Data store: S3
- Path: s3://your-raw-bucket/events/
- Output database: raw_events_db
- Table prefix: raw_

## Notes
- Crawler runs before Glue ETL job
- Schema evolution is handled automatically for additive changes
