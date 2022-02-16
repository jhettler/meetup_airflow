"""Example DAG demonstrating the usage of the BashOperator."""

from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.dummy import DummyOperator
from airflow.utils.task_group import TaskGroup

with DAG(
    dag_id='01_what_is_dag',
    schedule_interval='0 0 * * *',
    start_date=datetime(2022, 2, 15),
    catchup=False,
    dagrun_timeout=timedelta(minutes=60),
    tags=['dag', 'example'],
    params={"example_key": "example_value"},
    # "trigger_rule": "all_success",
    # "retries": 2,  # It means that it may run 1 times.
    # "max_active_runs": 1,  # Run only 1 instance of DAG
    # "retry_delay": timedelta(minutes=5),  # How long to wait to repeat    
) as dag:

    # task
    a = DummyOperator(
        task_id='first'
    )

    # with TaskGroup(group_id="middle_group") as processes:
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
    import pendulum
    local_tz = pendulum.timezone("Europe/Prague")
    dt = local_tz.convert(datetime(2022,2,15))
    dag.clear(start_date=dt, end_date=dt+timedelta(days=1))
    dag.run(start_date=dt, end_date=dt+timedelta(days=1))