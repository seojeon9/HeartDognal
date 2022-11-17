import unittest
from infra.spark_session import get_spark_session
from infra.util import cal_std_day

class MTest(unittest.TestCase):

    def test1(self):
        kafka_bootstrap_servers = 'localhost:9092'
        topic = 'test'

        df = get_spark_session() \
            .readStream\
            .format("kafka") \
            .option("kafka.bootstrap.servers", kafka_bootstrap_servers) \
            .option("startingOffsets", "latest") \
            .option("failOnDataLoss", "False") \
            .option("subscribe", topic) \
            .load()
        df.printSchema()

        df.writeStream \
            .format("json") \
            .outputMode("append") \
            .option('checkpointLocation', '/tmp/checkpoint') \
            .trigger(processingTime='30 seconds')  \
            .start('/corona_data/log/' + cal_std_day(0) + '.json') \
            .awaitTermination()

    def test2(self):
        path = '/corona_data/log/'
        co_patient_json = get_spark_session().read.json(path, encoding='UTF-8')
        co_patient_json.show()
        
if __name__ == "__main__":
    unittest.main()