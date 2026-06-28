from airflow import DAG
from airflow.operators.bash import BashOperator

from datetime import datetime

DBT_CMD = 'source ~/venv/bin/activate && cd ~/portfolio/entry/instacart/dbt'


with DAG(

    dag_id='instacart_pipeline',

    start_date=datetime(2026,1,1),

    schedule='@daily',

    catchup=False

) as dag:

    dbt_run = BashOperator(

        task_id='dbt_run',

        bash_command=f'{DBT_CMD} && dbt run'

    )

    dbt_test = BashOperator(

        task_id='dbt_test',

        bash_command=f'{DBT_CMD} && dbt test'

    )

    dbt_docs = BashOperator(

        task_id='dbt_docs',

        bash_command=f'{DBT_CMD} && dbt docs generate'

    )

    dbt_run >> dbt_test >> dbt_docs