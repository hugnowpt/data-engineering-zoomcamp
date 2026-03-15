from pyspark.sql import SparkSession
from pyspark.sql import functions as F

spark = SparkSession.builder \
    .appName("taxi") \
    .getOrCreate()

# read taxi data
df = spark.read.parquet("yellow_tripdata_2025-11.parquet")

# read zone lookup
zones = spark.read.option("header", "true").csv("taxi_zone_lookup.csv")

# join
df_join = df.join(
    zones,
    df.PULocationID == zones.LocationID
)

# find least frequent pickup zone
df_join.groupBy("Zone") \
    .count() \
    .orderBy("count") \
    .show(10)