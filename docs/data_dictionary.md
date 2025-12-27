# Data Dictionary — Event Data Pipeline

This document defines the structure, meaning, and expected values of the data produced by the AWS data pipeline. It serves as a reference for analysts, engineers, and downstream consumers.

---

## Dataset: processed_events

**Description:**  
Analytics-ready event data derived from raw application events. Stored in Parquet format in the processed S3 zone and queried via Amazon Athena.

**Grain:**  
One row per event.

---

## Column Definitions

| Column Name | Data Type | Description |
|-----------|----------|-------------|
| event_id | STRING | Unique identifier for the event |
| event_type | STRING | Type of event (e.g., `purchase`, `page_view`) |
| user_id | STRING | Unique identifier for the user |
| product_id | STRING | Identifier of the product associated with the event |
| amount | DOUBLE | Monetary amount associated with the event |
| currency | STRING | Currency code (ISO 4217, e.g., `USD`) |
| event_ts | TIMESTAMP | Timestamp when the event occurred |

---

## Business Rules

- `event_id` must be non-null
- `event_type` must be a known value
- `amount` must be ≥ 0
- `event_ts` must be in UTC

Records failing validation may be excluded or flagged during transformation.

---

## Example Records

```json
{
  "event_id": "e1",
  "event_type": "purchase",
  "user_id": "u101",
  "product_id": "p55",
  "amount": 49.99,
  "currency": "USD",
  "event_ts": "2025-12-26T20:00:00Z"
}

