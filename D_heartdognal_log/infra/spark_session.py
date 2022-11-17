import findspark
from pyspark.sql import SparkSession
from pyspark import SparkContext, SparkConf

findspark.init()
SPARK = None

def get_spark_session():

    global SPARK

    if SPARK:
        return SPARK
    
    spark_version = '3.2.2'
    findspark.add_packages(['org.apache.spark:spark-sql-kafka-0-10_2.12:3.2.2'
                            ,'org.apache.kafka:kafka-clients:3.2.1'])

    conf = SparkConf().setAppName('heartdognal-log')
    sc=SparkContext(conf=conf)
    
    SPARK = SparkSession(sc).builder.getOrCreate()
    return SPARK