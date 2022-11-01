from pyspark.sql.functions import col
from infra.jdbc import DataWarehouse, find_data, save_data
from infra.spark_session import get_spark_session
from infra.util import cal_std_day
import pandas as pd



class KindFeature:
    @ classmethod
    def transform(cls):
        path = '/roadpet/dog/kind/kind.json'
        path1 = '/roadpet/dog/kind/지식백과특징.csv'
        kind_json = get_spark_session().read.option("multiline","true").json(path, encoding='UTF-8').first()
        tmp = get_spark_session().createDataFrame(kind_json['response']['body']['items']['item'])
        kind_info = get_spark_session().read.csv(path1, encoding= 'UTF-8', header=True) # header=True 컬럼을 만들어주는 함수
        kind_info = kind_info.drop('색상','그룹구분','친화성')
        kind_info.show()
        tmp.show()
        # tmp = get_spark_session()

