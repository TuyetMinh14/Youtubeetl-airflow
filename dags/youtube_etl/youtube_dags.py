from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago

# Use absolute import instead of relative import
from youtube_etl.youtube_etl import youtube_etl

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
    'youtube_etl_dag',
    default_args=default_args,
    description='Youtube pipeline on airflow',
    schedule_interval=timedelta(days=1),
    catchup=False
)

run_etl = PythonOperator(
        task_id='youtube_etl_task',
        python_callable=youtube_etl,
        dag=dag
    )

run_etl  # Set task dependencies if you add more tasks


