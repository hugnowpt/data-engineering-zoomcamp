# Module 6 Homework – Batch Processing

This repository contains my solution for **Module 6:  Spark & Batch Processing** from the Data Engineering Zoomcamp.

For this homework we will be using the Yellow 2025-11 data from the official website:

`wget https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2025-11.parquet`

---

## Question 1: Install Spark and PySpark
- Install Spark
- Run PySpark
- Create a local spark session
- Execute spark.version.

#### Ans : 
Spark Version : 4.1.1


## Question 2: Yellow November 2025
Read the November 2025 Yellow into a Spark Dataframe.

Repartition the Dataframe to 4 partitions and save it to parquet.
What is the average size of the Parquet (ending with .parquet extension) Files that were created (in MB)?

[yellow_tripdata2025-11_Repartition.py](yellow_tripdata2025-11_Repartition.py)

#### Ans : 
25MB


## Question 3: Count records
How many taxi trips were there on the 15th of November?
Consider only trips that started on the 15th of November.

#### Ans : 
162,604


## Question 4: Longest trip
What is the length of the longest trip in the dataset in hours?

#### Ans : 
90.6


## Question 5:  User Interface
Spark's User Interface which shows the application's dashboard runs on which local port?

#### Ans : 
Port; 4040


## Question 6: Least frequent pickup location zone
Load the zone lookup data into a temp view in Spark:
`wget https://d37ci6vzurychx.cloudfront.net/misc/taxi_zone_lookup.csv`
Using the zone lookup data and the Yellow November 2025 data, what is the name of the LEAST frequent pickup location Zone?

#### Ans : 
- Governor's Island/Ellis Island/Liberty Island
- Arden Heights
