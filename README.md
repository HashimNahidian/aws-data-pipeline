# AWS Data Pipeline (S3 → Lambda → Glue → Athena)

This project demonstrates an end-to-end AWS data pipeline for ingesting raw JSON events, transforming them into analytics-ready Parquet, and querying them in Amazon Athena.

## Architecture
**Flow:** S3 (raw) → Lambda trigger → Glue Crawler → Glue ETL (JSON→Parquet) → Athena queries

See: `architecture/architecture.md`

## What this shows (Data Engineering skills)
- Data lake patterns (raw vs processed zones in S3)
- Event-driven ingestion with Lambda
- Schema discovery with Glue Crawlers
- ETL transformation and Parquet optimization with AWS Glue
- SQL analytics using Athena

## Repository structure
- `data/` sample inputs
- `lambda/` ingestion trigger + validation
- `glue/` ETL script + crawler notes
- `sql/` Athena table definitions + example queries
- `infra/terraform/` Infrastructure-as-Code (IaC)
- `docs/` runbook and data dictionary

## How to run (high-level)
1. Create S3 buckets for raw + processed data
2. Deploy Lambda trigger on raw bucket uploads
3. Run Glue Crawler to create a raw table
4. Run Glue Job to convert JSON → Parquet to processed bucket
5. Query processed Parquet with Athena

## Next steps (planned)
- Add partitioning by date (dt=YYYY-MM-DD)
- Add data quality checks (basic null/type validation)
- Add CI/CD for Terraform + Lambda packaging
