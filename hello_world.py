from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta


default_args = {
    'owner': 'chrisohiou57',
    'depends_on_past': False,
    'start_date': datetime(2021, 4, 21),
    'email': ['chrisohiou57@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(seconds=15)
}

# create the DAG instance
dag = DAG(
    dag_id='hello-world',
    default_args=default_args,
    schedule_interval=None,
    catchup=False
)

start_op = BashOperator(
    task_id='start',
    default_args=default_args,
    dag=dag,
    bash_command='echo "STARTED THE DAG RUN!"'
)

do_something_op = BashOperator(
    task_id='say-something',
    default_args=default_args,
    dag=dag,
    bash_command='echo "RAN ANOTHER BASH TASK!"'
)

start_op >> do_something_op
