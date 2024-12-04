



from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

# Define a simple function to print a message
def hello_world():
    print("Hello, Airflow 2.10.3!")

# Define the DAG
with DAG(
    dag_id="hello_world_dag",             # Unique DAG ID
    start_date=datetime(2023, 12, 1),    # Start date for the DAG
    schedule_interval="@daily",          # Run every day
    catchup=False,                       # Don't backfill past dates
) as dag:

    # Define a task
    hello_task = PythonOperator(
        task_id="hello_task",            # Unique task ID
        python_callable=hello_world,    # Function to call
    )

