from pyflink.table import EnvironmentSettings, TableEnvironment

env_settings = EnvironmentSettings.in_streaming_mode()
t_env = TableEnvironment.create(env_settings)

t_env.get_config().set("parallelism.default", "1")
t_env.get_config().set("execution.parallelism", "1")

# SOURCE (Kafka)
t_env.execute_sql("""
CREATE TABLE green_trips (
    lpep_pickup_datetime STRING,
    PULocationID INT,

    event_timestamp AS TO_TIMESTAMP(lpep_pickup_datetime, 'yyyy-MM-dd HH:mm:ss'),
    WATERMARK FOR event_timestamp AS event_timestamp - INTERVAL '5' SECOND
) WITH (
    'connector' = 'kafka',
    'topic' = 'green-trips',
    'properties.bootstrap.servers' = '07-streaming-redpanda-1:29092',
    'properties.group.id' = 'q5-group',
    'scan.startup.mode' = 'earliest-offset',
    'json.ignore-parse-errors' = 'true',
    'format' = 'json'
)
""")

# SINK (Postgres)
t_env.execute_sql("""
CREATE TABLE q5_results (
    session_start TIMESTAMP(3),
    session_end TIMESTAMP(3),
    PULocationID INT,
    num_trips BIGINT
) WITH (
    'connector' = 'jdbc',
    'url' = 'jdbc:postgresql://postgres:5432/postgres',
    'table-name' = 'q5_results',
    'username' = 'postgres',
    'password' = 'postgres'
)
""")

# SESSION WINDOW
t_env.execute_sql("""
INSERT INTO q5_results
SELECT
    SESSION_START(event_timestamp, INTERVAL '5' MINUTE),
    SESSION_END(event_timestamp, INTERVAL '5' MINUTE),
    PULocationID,
    COUNT(*) AS num_trips
FROM green_trips
GROUP BY
    PULocationID,
    SESSION(event_timestamp, INTERVAL '5' MINUTE)
""")