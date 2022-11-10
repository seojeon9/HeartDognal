import findspark
from pyspark.sql import SparkSession


def get_spark_session():
    findspark.init()
    return SparkSession.builder.getOrCreate()
