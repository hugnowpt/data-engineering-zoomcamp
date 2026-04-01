import pandas as pd
import json
from kafka import KafkaProducer
from time import time

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

url = "https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2025-10.parquet"
df = pd.read_parquet(url)

df = df[
    [
        'lpep_pickup_datetime',
        'lpep_dropoff_datetime',
        'PULocationID',
        'DOLocationID',
        'passenger_count',
        'trip_distance',
        'tip_amount',
        'total_amount'
    ]
]

df['lpep_pickup_datetime'] = df['lpep_pickup_datetime'].astype(str)
df['lpep_dropoff_datetime'] = df['lpep_dropoff_datetime'].astype(str)

t0 = time()

for _, row in df.iterrows():
    producer.send('green-trips', value=row.to_dict())

producer.flush()

t1 = time()

print(f'took {(t1 - t0):.2f} seconds')