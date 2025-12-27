# Architecture

## Zones
- **S3 Raw Zone:** stores incoming JSON events (immutable)
- **S3 Processed Zone:** stores transformed Parquet (analytics-ready)

## Event-driven ingestion
- S3 upload triggers a **Lambda** function
- Lambda logs event metadata and performs lightweight validation

## Schema + ETL
- **Glue Crawler** discovers schema for raw JSON and creates/updates Glue Data Catalog tables
- **Glue Job** transforms JSON → Parquet and writes to processed zone
- Output can be partitioned by date (planned enhancement)

## Query layer
- **Athena** queries processed Parquet tables for analytics

