from pyspark.sql import SparkSession
from pyspark.sql import functions as F

spark = SparkSession.builder \
    .appName("taxi") \
    .getOrCreate()

spark.sparkContext.setLogLevel("ERROR")

df = spark.read.parquet("yellow_tripdata_2025-11.parquet")

# คำนวณระยะเวลา trip
df_duration = df.withColumn(
    "trip_hours",
    (F.unix_timestamp("tpep_dropoff_datetime") -
     F.unix_timestamp("tpep_pickup_datetime")) / 3600
)

# หา trip ที่นานที่สุด
df_duration.select(F.max("trip_hours")).show()