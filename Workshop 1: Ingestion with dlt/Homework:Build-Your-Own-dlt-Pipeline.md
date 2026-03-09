
# Homework: Build Your Own dlt Pipeline

For this homework, build a dlt pipeline that loads NYC taxi trip data from a custom API into DuckDB and then answer some questions using the loaded data.

<img width="400" height="400" alt="image" src="https://github.com/user-attachments/assets/3bfe0a1e-96b2-45e6-b8b1-5a74f2d07fbd" />

---

## Question 1: What is the start date and end date of the dataset?

#### Solution : 
```sql
SELECT 
    MIN(trip_pickup_date_time),
    MAX(trip_pickup_date_time),
    MIN(trip_dropoff_date_time),
    MAX(trip_dropoff_date_time)
FROM nyc_taxi.nyc_taxi_data;
```

<img width="400" height="400" alt="image" src="https://github.com/user-attachments/assets/8d94557c-dff3-4b9a-8a53-768c7fcde8fc" />

#### Ans : 
2009-06-01 to 2009-07-01


## Question 2: What proportion of trips are paid with credit card?

#### Solution : 
```sql
SELECT 
    payment_type,
    ROUND(100.0 * COUNT(*) / SUM(COUNT(*)) OVER (), 2) AS percentage
FROM nyc_taxi.nyc_taxi_data
GROUP BY payment_type;
```
<img width="400" height="400" alt="image" src="https://github.com/user-attachments/assets/0fb460fb-8f96-49ae-9974-f830d82868f1" />

#### Ans : 
Credit	26.66%


## Question 3: What is the total amount of money generated in tips?

#### Solution : 
```sql
SELECT ROUND(SUM(tip_amt), 2) AS total_tips
FROM nyc_taxi.nyc_taxi_data;
```
<img width="400" height="400" alt="image" src="https://github.com/user-attachments/assets/56e844d4-7ff1-495b-bb85-49a27b86b227" />


#### Ans : 
$6,063.41
