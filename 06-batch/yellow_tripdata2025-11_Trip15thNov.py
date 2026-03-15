from pyspark.sql import SparkSession
from pyspark.sql import functions as F

# Create Spark session
spark = SparkSession.builder \
    .appName("taxi") \
    .getOrCreate()

# read parquet file
df = spark.read.parquet("yellow_tripdata_2025-11.parquet")

# filter only trip ที่เริ่มวันที่ 15 Nov 2025
df_filtered = df.filter(
    F.to_date("tpep_pickup_datetime") == "2025-11-15"
)

# count the number of records
trip_count = df_filtered.count()

print("Trips on 2025-11-15:", trip_count)