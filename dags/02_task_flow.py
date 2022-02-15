"""Example DAG demonstrating the usage of the BashOperator."""

from datetime import datetime, timedelta
from airflow.decorators import dag, task
from airflow.operators.bash import BashOperator

@dag(dag_id='02_task_flow', 
    schedule_interval='0 0 * * *', 
    start_date=datetime(2022, 2, 15), 
    catchup=False, 
    tags=['taskflow', 'example']
    )
def task_flow_example():

    @task()
    def get_first_value():
        return {"key1": "echo TaskFlow!"}

    @task()
    def get_another_value():
        return {"key2": "value2"}    

    @task(multiple_outputs=True)
    def merge(first, another):
        merged = {**first, **another}
        print(merged)
        return merged     

    op = BashOperator(task_id='test', 
                      bash_command=merge(get_first_value(), get_another_value())['key1']
                      )

tutorial_etl_dag = task_flow_example()

if __name__ == '__main__':
    tutorial_etl_dag.clear()
    tutorial_etl_dag.run(start_date=datetime(2022,2,15))
