# Module 4 Homework – dbt and analytics engineering

This repository contains my solution for **Module 4: dbt and analytics engineering** from the Data Engineering Zoomcamp.

---

## Question 1: dbt Lineage and Execution
If you run `dbt run --select int_trips_unioned`, what models will be built?

```sql
models/
├── staging/
│   ├── stg_green_tripdata.sql
│   └── stg_yellow_tripdata.sql
└── intermediate/
    └── int_trips_unioned.sql (depends on stg_green_tripdata & stg_yellow_tripdata)
```
#### Ans : 
`int_trips_unioned` only

## Question 2: dbt Tests

```sql
columns:
  - name: payment_type
    data_tests:
      - accepted_values:
          arguments:
            values: [1, 2, 3, 4, 5]
            quote: false
```
Your model `fct_trips` has been running successfully for months. A new value `6` now appears in the source data.
What happens when you run `dbt test --select fct_trips` ?

#### Ans : 
✅ dbt will fail the test, returning a non-zero exit code

## Question 3: Counting Records in fct_monthly_zone_revenue
After running your dbt project, query the `fct_monthly_zone_revenue` model.
What is the count of records in the model?

#### Solution : 
```sql
SELECT COUNT(*) 
FROM `zoomcamp-de-486714.dbt_nytaxi.fct_monthly_zone_revenue`;
```
#### Ans : 
12,184 row

## Question 4: Best Performing Zone for Green Taxis (2020)
Using the `fct_monthly_zone_revenue` table, find the pickup zone with the highest total revenue (revenue_monthly_total_amount) for Green taxi trips in 2020.
Which zone had the highest revenue? 

#### Solution : 
```sql
SELECT
  pickup_zone,
  SUM(revenue_monthly_total_amount) AS total_revenue
FROM `zoomcamp-de-486714.dbt_nytaxi.fct_monthly_zone_revenue`
WHERE service_type = 'Green'
  AND EXTRACT(YEAR FROM revenue_month) = 2020
GROUP BY pickup_zone
ORDER BY total_revenue DESC
LIMIT 1;
```

<img width="300" height="300" alt="image" src="https://github.com/user-attachments/assets/c699c5b4-371c-47a7-a87e-259710286410" />

#### Ans : 
East Harlem North

## Question 5: Green Taxi Trip Counts (October 2019)
Using the `fct_monthly_zone_revenue` table, what is the total number of trips (total_monthly_trips) for Green taxis in October 2019?

#### Solution : 
```sql
SELECT
  SUM(total_monthly_trips) AS total_trips
FROM `zoomcamp-de-486714.dbt_nytaxi.fct_monthly_zone_revenue`
WHERE service_type = 'Green'
  AND EXTRACT(YEAR FROM revenue_month) = 2019
  AND EXTRACT(MONTH FROM revenue_month) = 10;
```

#### Ans : 
421,509 
