import os
from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator

def download_dataset():
    # Ensure the directory exists inside the container
    output_path = "/opt/airflow/data"
    os.makedirs(output_path, exist_ok=True)

    # Defer imports to inside the callable so Airflow webserver doesn't crash 
    from kaggle.api.kaggle_api_extended import KaggleApi

    api = KaggleApi()
    api.authenticate()

    api.dataset_download_files(
        "matteo2002/retail-dataset",
        path=output_path,
        unzip=True,
    )


with DAG(
    dag_id="kaggle_download",
    start_date=datetime(2025, 1, 1),
    schedule=None,
    catchup=False,
) as dag:

    task = PythonOperator(
        task_id="download_dataset",
        python_callable=download_dataset,
    )