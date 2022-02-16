from airflow.models.dagbag import DagBag

dag_file_path = "/root/airflow/dags/01_what_is_dag.py"
dagbag = DagBag(dag_folder=dag_file_path)
dagbag.dags['01_what_is_dag'].task_dict['middle_1'].execute({})