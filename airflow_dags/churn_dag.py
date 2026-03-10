from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

# Default arguments for the DAG
default_args = {
    'owner': 'admin',
    'depends_on_past': False,
    'start_date': datetime(2024, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

def preprocess_step():
    print("Executing Data Preprocessing...")

def train_step():
    print("Executing Model Training and MLflow Logging...")

# Define the DAG
with DAG(
    'customer_churn_pipeline',
    default_args=default_args,
    description='Pipeline for Churn Prediction Project',
    schedule_interval='@daily',
    catchup=False
) as dag:

    task_preprocess = PythonOperator(
        task_id='preprocess_data',
        python_callable=preprocess_step
    )

    task_train = PythonOperator(
        task_id='train_model',
        python_callable=train_step
    )

    # Set the order of tasks
    task_preprocess >> task_train