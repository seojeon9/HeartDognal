from pyspark.sql.functions import col
from infra.jdbc import DataWarehouse, find_data, save_data
from infra.spark_session import get_spark_session
from infra.util import cal_std_day
import pandas as pd



class KindFeature:
    @ classmethod
    def transform(cls):
    

