# Module 3 Homework – Data-warehouse

This repository contains my solution for **Module 3: Data-warehouse** from the Data Engineering Zoomcamp.

---

## Question 1: Counting records
What is count of records for the 2024 Yellow Taxi Data?

```sql
SELECT COUNT(*) AS total_record
FROM `zoomcamp-de-486714.yellow_taxi_data.yellow_tripdata`;
```
#### Ans : 20,332,093 row

## Question 2: Data read estimation
Write a query to count the distinct number of PULocationIDs for the entire dataset on both the tables.
What is the estimated amount of data that will be read when this query is executed on the External Table and the Table?

#### External Table >
```sql
SELECT
  COUNT(DISTINCT PULocationID) AS distinct_pu_locations
FROM `zoomcamp-de-486714.yellow_taxi_data.yellow_tripdata_external`;
```
<img width="300" height="300" alt="image" src="https://github.com/user-attachments/assets/db862838-f305-4515-a070-63176f39a741" />

#### Regular Table >
```sql
SELECT
  COUNT(DISTINCT PULocationID) AS distinct_pu_locations
FROM `zoomcamp-de-486714.yellow_taxi_data.yellow_tripdata`;
```
<img width="300" height="300" alt="image" src="https://github.com/user-attachments/assets/8c03c721-b30d-4e9a-8a0b-3b59de0fc199" />

#### Ans : 0 MB for the External Table and 155.12 MB for the Materialized Table

## Question 3: Understanding columnar storage
Write a query to retrieve the PULocationID from the table (not the external table) in BigQuery. Now write a query to retrieve the PULocationID and DOLocationID on the same table.
Why are the estimated number of Bytes different?

#### PULocationID >
```sql
SELECT PULocationID
FROM `zoomcamp-de-486714.yellow_taxi_data.yellow_tripdata`;
```

#### PULocationID and DOLocationID >
```sql
SELECT
  PULocationID,
  DOLocationID
FROM `zoomcamp-de-486714.yellow_taxi_data.yellow_tripdata`;
```

💡 After executing each query, review the Execution details section and compare the Bytes processed.
The query that selects both `PULocationID` and `DOLocationID` processes more data than the query that selects only `PULocationID`.

#### Ans : BigQuery is a columnar database, and it only scans the specific columns requested in the query. Querying two columns (PULocationID, DOLocationID) requires reading more data than querying one column (PULocationID), leading to a higher estimated number of bytes processed.

## Question 4: Counting zero fare trips
How many records have a fare_amount of 0?
```sql
SELECT COUNT(*) AS zero_fare_trips
FROM `zoomcamp-de-486714.yellow_taxi_data.yellow_tripdata`
WHERE fare_amount = 0;
```
<img width="300" height="300" alt="image" src="https://github.com/user-attachments/assets/0b3e5653-2a44-4a3b-967f-2c60ead41a64" />

#### Ans : 8,333 

## Question 5: Partitioning and clustering
What is the best strategy to make an optimized table in Big Query if your query will always filter based on tpep_dropoff_datetime and order the results by VendorID (Create a new table with this strategy)

```sql
CREATE OR REPLACE TABLE `zoomcamp-de-486714.yellow_taxi_data.yellow_tripdata_optimized`
PARTITION BY DATE(tpep_dropoff_datetime)
CLUSTER BY VendorID
AS
SELECT *
FROM `zoomcamp-de-486714.yellow_taxi_data.yellow_tripdata`;
```

💡 The best strategy is to partition the table by `tpep_dropoff_datetime` to optimize filtering on dates, and cluster by `VendorID` to improve performance when ordering or grouping by vendor.

#### Ans : Partition by  tpep_dropoff_datetime  and Cluster on VendorID

## Question 6: Partition benefits
Write a query to retrieve the distinct VendorIDs between tpep_dropoff_datetime 2024-03-01 and 2024-03-15 (inclusive)

Use the materialized table you created earlier in your from clause and note the estimated bytes. 
Now change the table in the from clause to the partitioned table you created for question 5 and note the estimated bytes processed. 

#### Non-partitioned (materialized) table
```sql
SELECT DISTINCT VendorID
FROM `zoomcamp-de-486714.yellow_taxi_data.yellow_tripdata`
WHERE tpep_dropoff_datetime BETWEEN '2024-03-01' AND '2024-03-15';
```
<img width="300" height="300" alt="image" src="https://github.com/user-attachments/assets/ceca4abe-9c75-4642-9134-12945dd9285a" />

#### Partitioned table
```sql
SELECT DISTINCT VendorID
FROM `zoomcamp-de-486714.yellow_taxi_data.yellow_tripdata_optimized`
WHERE tpep_dropoff_datetime BETWEEN '2024-03-01' AND '2024-03-15';
```
<img width="300" height="300" alt="image" src="https://github.com/user-attachments/assets/3388aa10-618e-493c-ba62-b8a04cd10aa8" />

#### Ans : 310.24 MB for non-partitioned table and 26.84 MB for the partitioned table

## Question 7: External table storage
Where is the data stored in the External Table you created?

#### Ans : GCP Bucket

## Question 8: Clustering best practices
It is best practice in Big Query to always cluster your data

💡 Clustering should be applied selectively based on query patterns and table size. It is not a best practice to always cluster data in BigQuery.
#### Ans : False


