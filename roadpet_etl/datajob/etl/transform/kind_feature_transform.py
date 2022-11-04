from xml.dom.xmlbuilder import DocumentLS
from pyspark.sql.functions import col,split,when
from sqlalchemy import null
from infra.jdbc import DataWarehouse, save_data
from infra.spark_session import get_spark_session
from infra.util import cal_std_day
import pandas as pd
from pyspark.sql.types import *




class KindFeature:
    @ classmethod
    def transform(cls):
        path1 = './품종별 성격(성격단어추가).csv'
        kind_info = pd.read_csv(path1, encoding= 'cp949',index_col=0) 
        df_schema = StructType([StructField("품종", StringType(), True)
                        ,StructField("원산지", StringType(), True)
                        ,StructField("체고", StringType(), True)
                        ,StructField("체중", StringType(), True)
                        ,StructField("크기", StringType(), True)
                        ,StructField("외모", StringType(), True)
                        ,StructField("성격", StringType(), True)
                        ,StructField("추천성향", StringType(), True)
                        ,StructField("주요유의질병", StringType(), True)
                        ,StructField("털빠짐", StringType(), True)
                        ,StructField("집지키기", StringType(), True)
                        ,StructField("실내외구분", StringType(), True)
                        ,StructField("색상", StringType(), True)
                        ,StructField("그룹구분", StringType(), True)
                        ,StructField("친화성", StringType(), True)
                        ,StructField("성격단어", StringType(), True)])
        kind_info = get_spark_session().createDataFrame(kind_info, schema= df_schema)
        kind_info_df = kind_info.withColumn('추천주거형태', split(kind_info['추천성향'],',').getItem(0)).withColumn('추천연령대형태', split(kind_info['추천성향'],',').getItem(1)).withColumn('운동량', split(kind_info['추천성향'],',').getItem(2))                      
        kind_info_df = kind_info_df.select(
                col('품종').alias('KIND')
                ,col('원산지').alias('ORIGIN')
                ,col('체고').alias('HEIGHT')
                ,col('체중').alias('WEIGHT')
                ,col('크기').alias('SIZE')
                ,col('외모').alias('APPEARANCE')
                ,col('성격').alias('CHARACTER')
                ,col('추천주거형태').alias('RESIDENCE')
                ,col('주요유의질병').alias('DISEASE')
                ,col('털빠짐').alias('ALOPECIA')
                ,col('집지키기').alias('HOUSEKEEPING')
                ,col('실내외구분').alias('INOUTDOOR')
                ,col('추천연령대형태').alias('AGE_GROUP')
                ,col('운동량').alias('EXERCISE'))
        save_data(DataWarehouse, kind_info_df, 'KIND_FEATURE')

