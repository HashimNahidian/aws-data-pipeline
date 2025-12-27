import json
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def handler(event, context):
    """
    Triggered by S3 object creation events.
    Performs basic validation and logs metadata for downstream processing.
    """

    for record in event.get("Records", []):
        s3_info = record.get("s3", {})
        bucket = s3_info.get("bucket", {}).get("name")
        key = s3_info.get("object", {}).get("key")

        logger.info(
            json.dumps({
                "message": "New raw file ingested",
                "bucket": bucket,
                "key": key
            })
        )

    return {
        "statusCode": 200,
        "body": json.dumps("Ingestion event processed successfully")
    }
