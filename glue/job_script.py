import sys
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext

args = getResolvedOptions(sys.argv, ["JOB_NAME"])

sc = SparkContext()
glue_context = GlueContext(sc)
spark = glue_context.spark_session
job = Job(glue_context)
job.init(args["JOB_NAME"], args)

# Read raw JSON data from Glue Catalog
raw_df = glue_context.create_dynamic_frame.from_catalog(
    database="raw_events_db",
    table_name="raw_events"
)

# Convert to Spark DataFrame for transformations
df = raw_df.toDF()

# Example lightweight transformation
df_clean = df.filter(df.event_id.isNotNull())

# Write out as Parquet to processed zone
df_clean.write.mode("overwrite").parquet(
    "s3://your-processed-bucket/events/"
)

job.commit()
