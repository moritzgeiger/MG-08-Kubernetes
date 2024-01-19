from airflow.utils.dates import datetime

from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.models.baseoperator import chain

################### CONFIGURATION ###################
# Set the configs name

default_args = {
    'owner': 'Airflow',
    'start_date': datetime(2023, 9, 19),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 0
}

with DAG(
    dag_id='test_dag2',
    description=f'Runs the test dag',
    default_args=default_args,
    schedule_interval="0 3 1 * *", # every 3 months
    max_active_runs=1,
    catchup=False
    ) as dag:

    start = DummyOperator(
            task_id='start',
            )

    chain(start)
    