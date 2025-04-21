from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.db import create_session
from sqlalchemy import delete, select
from airflow.models.dataset import DatasetDagRunQueue
from utils.constant import CLIENT_LIST, SMTP_VARIABLE
from gmail import send_email
import pendulum
from template import digital_business_table_report_html_email


local_tz = pendulum.timezone("Asia/Bangkok")
dag_name = 'email_sending_dag'

dag = DAG(
    dag_name,
    schedule_interval='00 10 * * *',
    catchup=False,
    start_date=datetime(2025, 104, 14, tzinfo=local_tz),
    max_active_runs=1,
    tags=["gmail", "report"],
)

dag_send_email = PythonOperator(
    task_id="send_email",
    python_callable=send_email,
    dag=dag,
    op_kwargs={
        "to": CLIENT_LIST,
        "subject": "Test Email",
        "html_content": digital_business_table_report_html_email,
        "smtp_variable": SMTP_VARIABLE
    }
)

dag_send_email






