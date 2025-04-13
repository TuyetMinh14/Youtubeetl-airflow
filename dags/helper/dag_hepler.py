from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
import pendulum

from airflow.utils.db import create_session
from sqlalchemy import delete, select
from airflow.models.dataset import DatasetDagRunQueue

from utils.constant import DAG_ID


def reset_dataset_queues(dag_id):
    print(f"Resetting dataset queues for {dag_id}")
    with create_session() as session:
        session.execute(delete(DatasetDagRunQueue).where(DatasetDagRunQueue.target_dag_id == dag_id))
        result = session.execute(select(DatasetDagRunQueue).where(DatasetDagRunQueue.target_dag_id == dag_id)).all()
        print(result)
    return "OK"

doc_md_DAG = """
### DAG to reset dataset queues
This DAG clears the DatasetDagRunQueue for a specific DAG ID.
"""

# Define the DAG
dag = DAG(
    dag_id="reset_datasets",
    start_date=pendulum.now(),
    schedule_interval=None,
    catchup=False,
    doc_md=doc_md_DAG,
    tags=["helper","reset_dataset_queue"]
) 

reset_queue_task = PythonOperator(
    task_id="reset_dataset_queue_task",
    python_callable=reset_dataset_queues,
    dag=dag,
    op_kwargs={"dag_id": DAG_ID}
)

reset_queue_task  # Define task dependencies if needed
