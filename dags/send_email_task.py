from airflow import DAG
from airflow.operators.email_operator import EmailOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2022, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'email_notification_example',
    default_args=default_args,
    schedule_interval='@daily',
)

send_email_task = EmailOperator(
    task_id='send_email_task',
    to='adrien.crapart@gmail.com',
    subject='Airflow Notification',
    html_content='Hello, this is a notification from Airflow!',
    dag=dag
)

send_email_task
