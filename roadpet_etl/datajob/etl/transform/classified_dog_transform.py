from xml.dom.xmlbuilder import DocumentLS
from pyspark.sql.functions import col,split
from infra.jdbc import DataWarehouse, save_data,find_data
from infra.spark_session import get_spark_session
from infra.util import cal_std_day_yyyymmdd
from pyspark.sql.types import *

class ClassifiedDog:
    @ classmethod
    def transform(cls):
        path = '/roadpet/dog/kind/kind.json'
        path1 = find_data(DataWarehouse, 'KIND_FEATURE')
        path2 = find_data(DataWarehouse, 'ROADDOG_INFO')
        kind_json = get_spark_session().read.option("multiline","true").json(path,encoding='UTF-8').first()
        tmp = get_spark_session().createDataFrame(kind_json['response']['body']['items']['item'])
        tmp1 = path1.select('KIND')
        # tmp.show()
        tmp1.show()
        # path2.show()