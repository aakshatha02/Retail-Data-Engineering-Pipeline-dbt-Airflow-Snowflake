from airflow.providers.snowflake.hooks.snowflake import SnowflakeHook
from airflow.operators.python import PythonOperator
from datetime import datetime
from airflow import DAG
import csv


def upload_to_stage():
    hook = SnowflakeHook(snowflake_conn_id="snowflake_conn")
    hook.run("""
        USE DATABASE RETAIL;
        USE SCHEMA RAW;

        CREATE STAGE IF NOT EXISTS kaggle_stage;

        PUT file:///opt/airflow/data/*.csv
        @kaggle_stage
        AUTO_COMPRESS=FALSE
        OVERWRITE=TRUE;
    """)

def load_to_table():
    hook = SnowflakeHook(snowflake_conn_id="snowflake_conn")
    hook.run("""
        USE DATABASE RETAIL;
        USE SCHEMA RAW;
       
        TRUNCATE TABLE CUSTOMER;
        COPY INTO CUSTOMER 
        FROM @kaggle_stage/customers.csv
        FILE_FORMAT = (FORMAT_NAME = RETAIL.RAW.MY_CSV_FORMAT);

        TRUNCATE TABLE INVOICE_ITEMS;
        COPY INTO INVOICE_ITEMS 
        FROM @kaggle_stage/invoice_items.csv
        FILE_FORMAT = (FORMAT_NAME = RETAIL.RAW.MY_CSV_FORMAT);
        
        TRUNCATE TABLE PRODUCTS;
        COPY INTO PRODUCTS 
        FROM @kaggle_stage/products.csv
        FILE_FORMAT = (FORMAT_NAME = RETAIL.RAW.MY_CSV_FORMAT);
        
        TRUNCATE TABLE PURCHASES;
        COPY INTO PURCHASES 
        FROM @kaggle_stage/purchases.csv
        FILE_FORMAT = (FORMAT_NAME = RETAIL.RAW.MY_CSV_FORMAT);
        
    """)

with DAG(
    dag_id="load_to_snowflake",
    start_date=datetime(2025, 1, 1),
    schedule=None,
    catchup=False,
) as dag:
    
    upload_task = PythonOperator(
        task_id="upload_to_stage",
        python_callable=upload_to_stage
    )

    load_task = PythonOperator(
        task_id='load_to_table',
        python_callable=load_to_table
    )

    upload_task  >> load_task