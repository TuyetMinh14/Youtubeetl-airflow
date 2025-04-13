from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
import pendulum

from airflow.utils.db import create_session
from sqlalchemy import delete, select
from airflow.models.dataset import DatasetDagRunQueue

from utils.constant import client_list
from gmail import send_email

# Define the DAG
dag = DAG(
    dag_id="sending_gmail_test",
    start_date=pendulum.now(),
    schedule_interval=None,
    catchup=False,
    tags=["gmail","reporting"]
) 
smtp_variable = {
    "smtp_host": "smtp.gmail.com",
    "smtp_port": 465,
    "smtp_user": "thuanh14403@gmail.com",
    "smtp_password": "nfzk fofw hqjj extn",
    "smtp_mail_from": "thuanh14403@gmail.com",
    "smtp_ssl": True,        
    "smtp_starttls": False 
}
dag_send_email = PythonOperator(
    task_id="send_email",
    python_callable=send_email,
    dag=dag,
    op_kwargs={
        "to": client_list,
        "subject": "Test Email",
        "html_content": "Trẻ trâu liên quân",
        "smtp_variable": smtp_variable
    }
)

dag_send_email






