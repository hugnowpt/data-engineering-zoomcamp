from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id="retail_pipeline",
    start_date=datetime(2024, 1, 1),
    schedule_interval="*/2 * * * *",
    catchup=False,
) as dag:

    dbt_staging = BashOperator(
        task_id="dbt_staging",
        bash_command="cd /opt/airflow/dbt/retail_dbt && dbt run --select staging --profiles-dir /opt/airflow/dbt/retail_dbt"
    )

    dbt_marts = BashOperator(
        task_id="dbt_marts",
        bash_command="cd /opt/airflow/dbt/retail_dbt && dbt run --select marts --profiles-dir /opt/airflow/dbt/retail_dbt"
    )

    dbt_staging >> dbt_marts