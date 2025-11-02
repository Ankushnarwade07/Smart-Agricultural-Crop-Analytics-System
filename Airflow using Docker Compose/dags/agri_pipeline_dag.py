from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'ankush',
    'retries': 1,
    'retry_delay': timedelta(minutes=2),
}

with DAG(
    dag_id='agri_pipeline_dag',
    default_args=default_args,
    description='Crop Recommendation ETL + Model Inference',
    schedule_interval=None,
    start_date=datetime(2025, 11, 1),
    catchup=False,
) as dag:

    run_etl = BashOperator(
        task_id='run_crop_etl',
        bash_command='python3 /opt/airflow/scripts/agri_etl_pipeline.py'
    )

    run_etl
