from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.providers.google.cloud.transfers.gcs_to_bigquery import GCSToBigQueryOperator
from datetime import datetime

PROJECT_ID = "retail-oltp-analytics-pipeline"
BUCKET_NAME = "retail-oltp-analytics-pipeline"
DATASET_NAME = "retail_dataset"

with DAG(
    dag_id="retail_pipeline",
    start_date=datetime(2024, 1, 1),
    schedule_interval="*/2 * * * *",
    catchup=False,
) as dag:

    load_to_bigquery = GCSToBigQueryOperator(
        task_id="load_gcs_to_bigquery",
        bucket=BUCKET_NAME,           
        source_objects=["raw/sales_raw_oltp.csv"], 
        destination_project_dataset_table=f"{PROJECT_ID}.{DATASET_NAME}.sales_raw_oltp",
        source_format="CSV",
        write_disposition="WRITE_TRUNCATE",       
        skip_leading_rows=1,                     
        gcp_credentials="/opt/airflow/dbt/keyfile.json",
        autodetect=True,                          
    )

    dbt_staging = BashOperator(
        task_id="dbt_staging",
        bash_command="cd /opt/airflow/dbt/retail_dbt && dbt run --select staging --profiles-dir /opt/airflow/dbt/retail_dbt"
    )

    dbt_marts = BashOperator(
        task_id="dbt_marts",
        bash_command="cd /opt/airflow/dbt/retail_dbt && dbt run --select marts --profiles-dir /opt/airflow/dbt/retail_dbt"
    )

    load_to_bigquery >> dbt_staging >> dbt_marts
