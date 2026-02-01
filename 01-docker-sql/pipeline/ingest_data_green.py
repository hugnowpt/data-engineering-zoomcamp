import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "postgresql://root:root@pgdatabase:5432/ny_taxi"
)

# อ่าน parquet จากไฟล์ที่ mount มา
df = pd.read_parquet("/data/green_tripdata_2025-11.parquet")

df.to_sql(
    name="green_taxi_trips_2025_11",
    con=engine,
    if_exists="replace",
    index=False
)

zones = pd.read_csv("/data/taxi_zone_lookup.csv")

zones.to_sql(
    name="taxi_zone_lookup",
    con=engine,
    if_exists="replace",
    index=False
)
