from xml.dom.xmlbuilder import DocumentLS
from pyspark.sql.functions import col,split
from infra.jdbc import DataWarehouse, save_data,find_data
from infra.spark_session import get_spark_session
from infra.util import cal_std_day_yyyymmdd
from pyspark.sql.types import *

class ClassifiedDog:
    @ classmethod
    def transform(cls):
        path = find_data(DataWarehouse, 'KIND_FEATURE')
        path1 = find_data(DataWarehouse, 'ROADDOG_INFO')
        tmp = path.select('KIND')
        tmp1 = path1.select('KIND_NM')

        tmp.show()
        tmp1.show()
