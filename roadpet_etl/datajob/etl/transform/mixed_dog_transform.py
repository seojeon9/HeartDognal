from xml.dom.xmlbuilder import DocumentLS
from pyspark.sql.functions import col,split
from infra.jdbc import DataWarehouse, save_data,find_data
from infra.spark_session import get_spark_session
from infra.util import cal_std_day_yyyymmdd
from pyspark.sql.types import *

class MixedDog:
    @ classmethod
    def transform(cls):
        path = find_data(DataWarehouse, 'ROADDOG_INFO')
        mix = path.select('KIND_NM').where(path.KIND_NM =='믹스견')
        mix.show()