from infra.spark_session import get_spark_session
from infra.util import cal_std_day
from datetime import date, datetime
from pyspark.sql import Row
from pyspark.sql.types import *
import json

# foreachBatch : Spark Streaming 배치마다 수행할 작업을 콜백함수로 넘겨줄 수있다.
# https://spark.apache.org/docs/3.3.1/structured-streaming-programming-guide.html#foreachbatch

kafka_bootstrap_servers = 'localhost:9092'


if __name__ == "__main__":
    topic = 'heartdognal-log'
    dfs = get_spark_session() \
        .readStream \
        .format("kafka") \
        .option("kafka.bootstrap.servers", kafka_bootstrap_servers) \
        .option("startingOffsets", "latest") \
        .option("failOnDataLoss", "False") \
        .option("subscribe", topic) \
        .load()

    dfs = dfs.selectExpr("CAST(value as STRING)").alias("log")
    
    query = dfs.writeStream \
        .format("json") \
        .outputMode("append") \
        .option('checkpointLocation', '/tmp/log/checkpoint/') \
        .option("path", "/roadpet/log") \
        .trigger(processingTime='20 seconds')  \
        .start() \
        
    query.awaitTermination()




