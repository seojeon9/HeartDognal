from datetime import datetime, timedelta
from textwrap import dedent

# The DAG object; we'll need this to instantiate a DAG
from airflow import DAG

# Operators; we need this to operate!
from airflow.operators.bash import BashOperator
with DAG(
    'movie_etl',
    # These args will get passed on to each operator
    # You can override them on a per-task basis during operator initialization
    default_args={
        'depends_on_past': False,
        'email': ['s.zisu0417@gmail.com'],
        'email_on_failure': False,
        'email_on_retry': False,
        'retries': 2,
        'retry_delay': timedelta(minutes=20),
    },
    description='Movie ETL Project',
    # schedule=timedelta(days=1),
    start_date=datetime(2022, 10, 5, 4, 30),
    catchup=False,
    tags=['movie_etl'],
) as dag:

    # t1, t2 and t3 are examples of tasks created by instantiating operators
    t1 = BashOperator(
        task_id='extract_daily_boxoffice',
        cwd='/home/big/study/movie_etl',
        bash_command='python3 main.py extract daily_boxoffice',
    )

    t2 = BashOperator(
        task_id='transform_daily_boxoffice',
        cwd='/home/big/study/movie_etl',
        bash_command='python3 main.py transform daily_boxoffice',
        # retries=3,
    )

    t3 = BashOperator(
        task_id='extract_movie_detail',
        cwd='/home/big/study/movie_etl',
        bash_command='python3 main.py extract movie_detail',
    )

    t4 = BashOperator(
        task_id='transform_movie_detail',
        cwd='/home/big/study/movie_etl',
        bash_command='python3 main.py transform movie_detail',
    )

    t5 = BashOperator(
        task_id='extract_naver_datalab',
        cwd='/home/big/study/movie_etl',
        bash_command='python3 main.py extract naver_datalab',
    )

    t6 = BashOperator(
        task_id='extract_naver_search',
        cwd='/home/big/study/movie_etl',
        bash_command='python3 main.py extract naver_search',
    )

    t7 = BashOperator(
        task_id='extract_movie_score',
        cwd='/home/big/study/movie_etl',
        bash_command='python3 main.py extract movie_score',
    )

    t8 = BashOperator(
        task_id='transform_movie_score',
        cwd='/home/big/study/movie_etl',
        bash_command='python3 main.py transform movie_score',
    )

    t9 = BashOperator(
        task_id='transform_movie_url_actor',
        cwd='/home/big/study/movie_etl',
        bash_command='python3 main.py transform movie_url_actor',
    )

    t10 = BashOperator(
        task_id='transform_naver_datalab',
        cwd='/home/big/study/movie_etl',
        bash_command='python3 main.py transform naver_datalab',
    )

    t11 = BashOperator(
        task_id='datamart_movie_hit',
        cwd='/home/big/study/movie_etl',
        bash_command='python3 main.py datamart movie_hit',
    )

    t12 = BashOperator(
        task_id='datamart_movie',
        cwd='/home/big/study/movie_etl',
        bash_command='python3 main.py datamart movie',
    )

    t13 = BashOperator(
        task_id='datamart_actor',
        cwd='/home/big/study/movie_etl',
        bash_command='python3 main.py datamart actor',
    )

    t14 = BashOperator(
        task_id='datamart_company',
        cwd='/home/big/study/movie_etl',
        bash_command='python3 main.py datamart company',
    )

    t15 = BashOperator(
        task_id='datamart_genre',
        cwd='/home/big/study/movie_etl',
        bash_command='python3 main.py datamart genre',
    )

    t16 = BashOperator(
        task_id='datamart_movieAudi',
        cwd='/home/big/study/movie_etl',
        bash_command='python3 main.py datamart movieAudi',
    )

    t17 = BashOperator(
        task_id='datamart_movieRank',
        cwd='/home/big/study/movie_etl',
        bash_command='python3 main.py datamart movieRank',
    )

    t18 = BashOperator(
        task_id='datamart_movieSales',
        cwd='/home/big/study/movie_etl',
        bash_command='python3 main.py datamart movieSales',
    )

    t19 = BashOperator(
        task_id='datamart_movieScore',
        cwd='/home/big/study/movie_etl',
        bash_command='python3 main.py datamart movieScore',
    )

    t20 = BashOperator(
        task_id='datamart_movieScrn',
        cwd='/home/big/study/movie_etl',
        bash_command='python3 main.py datamart movieScrn',
    )

    t21 = BashOperator(
        task_id='datamart_movieSearch',
        cwd='/home/big/study/movie_etl',
        bash_command='python3 main.py datamart movieSearch',
    )

    t22 = BashOperator(
        task_id='datamart_movieShow',
        cwd='/home/big/study/movie_etl',
        bash_command='python3 main.py datamart movieShow',
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

    t1 >> t2 >> t3 >> t4 >> [t5, t6] 
    t5 >> [t9, t10] >> t7  >> t8 >> t11 >> t12 >> [t13, t14, t15, t16, t17, t18, t19, t20, t21, t22]
    t6 >> [t9, t10]

    #t1 >> t2 >> t3 >> t4 >> [t5, t6] >> [t9, t10] >> t7 >> t8 >> t11 > t12 >> [t13, t14, t15, t16, t17, t18, t19, t20]