from pyspark.sql import SparkSession

# Import additional libraries
from pyspark.sql.functions import col, to_timestamp, monotonically_increasing_id, to_date, when
from pyspark.sql.types import *
from datetime import datetime
import sys
from awsglue.utils import getResolvedOptions

# Create an array of the job parameters
args = getResolvedOptions(sys.argv, ['s3_bucket_name'])

# Initialize a SparkSession
spark = SparkSession.builder \
    .appName("IcebergIntegration") \
    .config("spark.sql.extensions", "org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions") \
    .config("spark.sql.catalog.glue_catalog", "org.apache.iceberg.spark.SparkCatalog") \
    .config("spark.sql.catalog.glue_catalog.warehouse", "s3://" + args['s3_bucket_name'] + "/iceberg/") \
    .config("spark.sql.catalog.glue_catalog.catalog-impl", "org.apache.iceberg.aws.glue.GlueCatalog") \
    .config("spark.sql.catalog.glue_catalog.io-impl", "org.apache.iceberg.aws.s3.S3FileIO") \
    .getOrCreate()
    
# Create sample data
data = [
        ("1", "Chris", "2020-01-01", datetime.strptime('2020-01-01 00:00:00', '%Y-%m-%d %H:%M:%S')),
        ("2", "Will", "2020-01-01", datetime.strptime('2020-01-01 00:00:00', '%Y-%m-%d %H:%M:%S')),
        ("3", "Emma", "2020-01-01", datetime.strptime('2020-01-01 00:00:00', '%Y-%m-%d %H:%M:%S')),
        ("4", "John", "2020-01-01", datetime.strptime('2020-01-01 00:00:00', '%Y-%m-%d %H:%M:%S')),
        ("5", "Eric", "2020-01-01", datetime.strptime('2020-01-01 00:00:00', '%Y-%m-%d %H:%M:%S')),
        ("6", "Adam", "2020-01-01", datetime.strptime('2020-01-01 00:00:00', '%Y-%m-%d %H:%M:%S'))
]

schema = StructType([
        StructField("id", StringType(), False),
        StructField("name", StringType(), False), 
        StructField("create_date", StringType(), False),             
        StructField("last_update_time", TimestampType(), False)
])

inputDf = spark.createDataFrame(data=data,schema=schema)

# Write sample data to S3 as Iceberg
inputDf.createOrReplaceTempView("tmp_inputDf")

query = f"""
CREATE TABLE glue_catalog.iceberg.sampledataicebergtable
USING iceberg
TBLPROPERTIES ("format-version"="2")
AS SELECT * FROM tmp_inputDf
"""

spark.sql(query)

# Read sample data 
query = f"""SELECT * FROM glue_catalog.iceberg.sampledataicebergtable"""

#resultsDf = spark.sql(query)
#resultsDf.show()
