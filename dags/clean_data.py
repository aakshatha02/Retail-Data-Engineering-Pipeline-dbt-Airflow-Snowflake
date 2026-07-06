from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

default_args = {
    'start_date': datetime(2024, 1, 1),
}

with DAG(
    dag_id='dbt_snowflake_pipeline',
    schedule='@daily',
    catchup=False,
    default_args=default_args,
    tags=['dbt', 'snowflake'],
) as dag:

    dbt_run_customers = BashOperator(
        task_id='dbt_run_customers',
        bash_command="""
        cd /opt/airflow/dbt && dbt run --select stg_customers
        """
    )

    dbt_run_invoiceitems = BashOperator(
        task_id='dbt_run_invoiceitems',
        bash_command="""
        cd /opt/airflow/dbt && dbt run --select stg_invoice_items
        """
    )

    dbt_run_products = BashOperator(
        task_id="dbt_run_products",
        bash_command="""
        cd /opt/airflow/dbt && dbt run --select stg_products
        """
    )

    dbt_run_purchase = BashOperator(
        task_id="dbt_run_purchases",
        bash_command="""
        cd /opt/airflow/dbt && dbt run --select stg_purchases
        """
    )



