from pyflink.table import EnvironmentSettings, TableEnvironment

env_settings = EnvironmentSettings.in_streaming_mode()
t_env = TableEnvironment.create(env_settings)

t_env.get_config().set("parallelism.default", "1")

# source (Kafka)
t_env.execute_sql("""
CREATE TABLE green_trips (
    lpep_pickup_datetime VARCHAR,
    PULocationID INT,
    event_timestamp AS TO_TIMESTAMP(lpep_pickup_datetime, 'yyyy-MM-dd HH:mm:ss'),
    WATERMARK FOR event_timestamp AS event_timestamp - INTERVAL '5' SECOND
) WITH (
    'connector' = 'kafka',
    'topic' = 'green-trips',
    'properties.bootstrap.servers' = 'redpanda:29092',
    'properties.group.id' = 'q4-group',
     'scan.startup.mode' = 'earliest-offset',  
    'format' = 'json',
    'json.ignore-parse-errors' = 'true'
)
""")

# sink (Postgres)
t_env.execute_sql("""
CREATE TABLE q4_results (
    window_start TIMESTAMP,
    PULocationID INT,
    num_trips BIGINT
) WITH (
    'connector' = 'jdbc',
    'url' = 'jdbc:postgresql://postgres:5432/postgres',
    'table-name' = 'q4_results',
    'username' = 'postgres',
    'password' = 'postgres'
)
""")

# query (หัวใจของข้อ)
t_env.execute_sql("""
INSERT INTO q4_results
SELECT
    TUMBLE_START(event_timestamp, INTERVAL '5' MINUTE) AS window_start,
    PULocationID,
    COUNT(*) AS num_trips
FROM green_trips
GROUP BY
    TUMBLE(event_timestamp, INTERVAL '5' MINUTE),
    PULocationID
""")