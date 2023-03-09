from datetime import datetime, timedelta
from textwrap import dedent

# The DAG object; we'll need this to instantiate a DAG
from airflow import DAG

# Operators; we need this to operate!
from airflow.operators.bash import BashOperator
with DAG(
    'roadpet_etl',
    # These args will get passed on to each operator
    # You can override them on a per-task basis during operator initialization
    default_args={
        'depends_on_past': False,
        'email': ['s.zisu0417@gmail.com'],
        'email_on_failure': False,
        'email_on_retry': False,
        'retries': 2,
        'retry_delay': timedelta(minutes=2),
    },
    description='ROADPET ETL Project',
    # schedule=timedelta(days=1),
    start_date=datetime(2022, 11, 14, 4, 30),
    catchup=False,
    tags=['roadpet_etl'],
) as dag:

    # t1, t2 and t3 are examples of tasks created by instantiating operators
    t1 = BashOperator(
        task_id='extract_road_dog',
        cwd='/home/big/study/roadpet_etl',
        bash_command='python3 main.py extract roaddog_info',
    )

    t2 = BashOperator(
        task_id='transform_road_dog',
        cwd='/home/big/study/roadpet_etl',
        bash_command='python3 main.py transform roaddog_info',
    )

    t3 = BashOperator(
        task_id='transform_finished_dog',
        cwd='/home/big/study/roadpet_etl',
        bash_command='python3 main.py transform finished_dog',
    )


    t4 = BashOperator(
        task_id='modeling_road_dog',
        cwd='/home/big/study/roadpet_etl',
        bash_command='python3 main.py modeling content_sim_preprocess',
    )

    t1.doc_md = dedent(
        """\
    #### Task Documentation
    You can document your task using the attributes `doc_md` (markdown),
    `doc` (plain text), `doc_rst`, `doc_json`, `doc_yaml` which gets
    rendered in the UI's Task Instance Details page.
    ![img](http://montcs.bloomu.edu/~bobmon/Semesters/2012-01/491/import%20soul.png)
    **Image Credit:** Randall Munroe, [XKCD](https://xkcd.com/license.html)
    """
    )

    dag.doc_md = __doc__  # providing that you have a docstring at the beginning of the DAG; OR
    dag.doc_md = """
    This is a documentation placed anywhere
    """  # otherwise, type it like this
    templated_command = dedent(
        """
    {% for i in range(5) %}
        echo "{{ ds }}"
        echo "{{ macros.ds_add(ds, 7)}}"
    {% endfor %}
    """
    )

    t1 >> t2 >> t3 >> t4