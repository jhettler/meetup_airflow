FROM python:3.8.12

# Airflow needs a home. `~/airflow` is the default, but you can put it
# somewhere else if you prefer (optional)
ENV AIRFLOW_HOME "~/airflow"
ENV AIRFLOW_VERSION "2.2.3"
ENV PYTHON_VERSION="3.8"
# For example: 3.8,
ENV CONSTRAINT_URL "https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt"
# For example: https://raw.githubusercontent.com/apache/airflow/constraints-2.2.3/constraints-3.8.txt

RUN pip install apache-airflow==${AIRFLOW_VERSION} --constraint ${CONSTRAINT_URL}