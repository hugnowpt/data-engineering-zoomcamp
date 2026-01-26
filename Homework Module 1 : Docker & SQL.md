# Module 1 Homework – Docker & SQL

This repository contains my solution for **Module 1: Docker & SQL**
from the Data Engineering Zoomcamp.

---

## Question 1: Understanding Docker Images

Run Docker with the `python:3.13` image and check the pip version.

#### Command
```bash
docker run -it --rm python:3.13 bash
pip --version
```

#### Answer
pip 25.3

## Question 2. Understanding Docker networking and docker-compose
Given the following docker-compose.yaml, what is the hostname and port that pgadmin should use to connect to the postgres database?
```bash
services:
  db:
    container_name: postgres
    image: postgres:17-alpine
    environment:
      POSTGRES_USER: 'postgres'
      POSTGRES_PASSWORD: 'postgres'
      POSTGRES_DB: 'ny_taxi'
    ports:
      - '5433:5432'
    volumes:
      - vol-pgdata:/var/lib/postgresql/data

  pgadmin:
    container_name: pgadmin
    image: dpage/pgadmin4:latest
    environment:
      PGADMIN_DEFAULT_EMAIL: "pgadmin@pgadmin.com"
      PGADMIN_DEFAULT_PASSWORD: "pgadmin"
    ports:
      - "8080:80"
    volumes:
      - vol-pgadmin_data:/var/lib/pgadmin

volumes:
  vol-pgdata:
    name: vol-pgdata
  vol-pgadmin_data:
    name: vol-pgadmin_data
```
#### Answer
db:5432

## Question 3. Counting short trips
For the trips in November 2025 (lpep_pickup_datetime between '2025-11-01' and '2025-12-01', exclusive of the upper bound), how many trips had a trip_distance of less than or equal to 1 mile?

#### SQL
```bash
SELECT COUNT(*) AS short_trips
FROM public.green_taxi_trips_2025_11
WHERE
    trip_distance <= 1
    AND lpep_pickup_datetime >= '2025-11-01'
    AND lpep_pickup_datetime < '2025-12-01';
```
#### Answer
- 8,007

## Question 4. Longest trip for each day
Which was the pick up day with the longest trip distance? Only consider trips with trip_distance less than 100 miles (to exclude data errors). Use the pick up time for your calculations.

#### SQL
```bash
SELECT
    DATE(lpep_pickup_datetime) AS pickup_date,
    MAX(trip_distance) AS max_trip_distance
FROM public.green_taxi_trips_2025_11
WHERE
    trip_distance < 100
    AND lpep_pickup_datetime >= '2025-11-01'
    AND lpep_pickup_datetime < '2025-12-01'
GROUP BY pickup_date
ORDER BY max_trip_distance DESC
LIMIT 1;
```
#### Answer
- pickup_date ; 2025-11-14 
- max_trip_distance ; 88.03


## Question 5. Biggest pickup zone
Which was the pickup zone with the largest total_amount (sum of all trips) on November 18th, 2025?

#### SQL
```bash
SELECT
    zpu."Zone" AS pickup_zone,
    SUM(t.total_amount) AS total_revenue
FROM public.green_taxi_trips_2025_11 t
JOIN public.taxi_zone_lookup zpu
    ON t."PULocationID" = zpu."LocationID"
WHERE
    DATE(t.lpep_pickup_datetime) = '2025-11-18'
GROUP BY pickup_zone
ORDER BY total_revenue DESC
LIMIT 1;
```
#### Answer
- pickup_zone ; East Harlem North
- total_revenue ; 9281.19

## Question 6. Largest tip
For the passengers picked up in the zone named "East Harlem North" in November 2025, which was the drop off zone that had the largest tip?
Note: it's tip , not trip. We need the name of the zone, not the ID.

#### SQL
```bash
SELECT
    zdo."Zone" AS dropoff_zone,
    SUM(t.tip_amount) AS total_tip
FROM public.green_taxi_trips_2025_11 t
JOIN public.taxi_zone_lookup zpu
    ON t."PULocationID" = zpu."LocationID"
JOIN public.taxi_zone_lookup zdo
    ON t."DOLocationID" = zdo."LocationID"
WHERE
    zpu."Zone" = 'East Harlem North'
    AND t.lpep_pickup_datetime >= '2025-11-01'
    AND t.lpep_pickup_datetime < '2025-12-01'
    AND zdo."Zone" IN (
        'JFK Airport',
        'Yorkville West',
        'East Harlem North',
        'LaGuardia Airport'
    )
GROUP BY dropoff_zone
ORDER BY total_tip DESC
LIMIT 1;
```
#### Answer
- dropoff_zone ; Yorkville West
- total_trip ; 2403


