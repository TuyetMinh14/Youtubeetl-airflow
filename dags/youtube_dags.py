from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator 
from airflow.utils.dates import days_ago
from youtube_etl import youtube_etl


# These args will get passed on to each operator
# You can override them on a per-task basis during operator initialization
default_args={
    "owner":"Lucy",
    'depends_on_past': False,
    'email': ['lucybieber2003@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
    'start_date':datetime(2023,9,17)
}

dag = DAG(
    'youtube_dags',
    default_args=default_args,
    description = 'Youtube pipline on airflow'
)

run_etl = PythonOperator(
    task_id = 'youtube_task',
    python_callable = youtube_etl,
    dag = dag
)

run_etl


