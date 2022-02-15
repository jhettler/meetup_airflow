"""Example DAG demonstrating the usage of the BashOperator."""

from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.dummy import DummyOperator

with DAG(
    dag_id='01_what_is_dag',
    schedule_interval='0 0 * * *',
    start_date=datetime(2022, 2, 15),
    catchup=False,
    dagrun_timeout=timedelta(minutes=60),
    tags=['dag', 'example'],
    params={"example_key": "example_value"},
) as dag:

    # task
    a = DummyOperator(
        task_id='first'
    )

    b1 = BashOperator(
        task_id='middle_1',
        bash_command='echo 1'
    )

    b2 = BashOperator(
        task_id='middle_2',
        bash_command='echo 1',
    )

    c = DummyOperator(
        task_id='last'
    )

    a >> b1 >> b2 >> c
    # a >> [b1,b2] >> c
    # a.set_downstream([b1,b2])
    # c.set_upstream([b1,b2])

if __name__ == "__main__":
    dag.cli()