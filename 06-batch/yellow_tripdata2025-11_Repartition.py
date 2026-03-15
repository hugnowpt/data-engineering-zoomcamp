from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("taxi") \
    .getOrCreate()

df = spark.read.parquet("yellow_tripdata_2025-11.parquet")
df = df.repartition(4)
df.write.parquet("yellow", mode="overwrite")
print("done")