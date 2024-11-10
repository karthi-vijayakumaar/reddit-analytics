from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import sys
sys.path.append('./../scripts')
from fetch_reddit_data import fetch_reddit_posts
from process_data import process_reddit_data

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 11, 9),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'reddit_analytics',
    default_args=default_args,
    description='Reddit data analytics pipeline',
    schedule_interval='@daily',
)

fetch_data = PythonOperator(
    task_id='fetch_reddit_data',
    python_callable=fetch_reddit_posts,
    dag=dag,
)

process_data = PythonOperator(
    task_id='process_reddit_data',
    python_callable=process_reddit_data,
    dag=dag,
)

fetch_data >> process_data