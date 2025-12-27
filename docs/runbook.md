```markdown
# Data Pipeline Runbook

This runbook provides operational guidance for monitoring, troubleshooting, and maintaining the AWS data pipeline.

---

## Pipeline Overview

**Flow:**  
S3 (raw) → Lambda trigger → Glue Crawler → Glue ETL → S3 (processed) → Athena

---

## Normal Operation

### Ingestion
- Raw JSON files are uploaded to the raw S3 bucket
- S3 event triggers the Lambda ingestion function
- Lambda logs file metadata to CloudWatch

### Transformation
- Glue Crawler detects schema and updates the Data Catalog
- Glue Job converts raw JSON into Parquet format
- Processed data is written to the processed S3 zone

### Analytics
- Athena queries processed Parquet tables
- Queries are optimized for read-heavy workloads

---

## Monitoring

### Lambda
- CloudWatch Logs for ingestion events
- Monitor invocation errors and throttles

### Glue
- Job run status in AWS Glue console
- Monitor job duration and failures

### S3
- Verify raw and processed file counts
- Check for unexpected file growth or missing data

---

## Common Issues & Troubleshooting

### Issue: Glue job fails
**Steps:**
1. Check Glue job logs in CloudWatch
2. Validate schema compatibility
3. Confirm S3 permissions and paths

---

### Issue: Athena query returns no data
**Steps:**
1. Verify Glue Crawler ran successfully
2. Confirm processed Parquet files exist
3. Check table location and partitions

---

### Issue: Missing or malformed events
**Steps:**
1. Inspect raw JSON files
2. Review Lambda logs
3. Confirm validation rules

---

## Recovery Procedures

- Raw data is immutable and can be reprocessed
- Glue jobs can be rerun safely
- Athena tables can be dropped and recreated if needed

---

## Change Management

- Schema changes should be documented in the data dictionary
- Breaking changes require downstream notification
- All infrastructure changes should be made via IaC (Terraform)

