from datetime import datetime
import json
import pandas as pd
from pyspark.sql.functions import split, col, when, concat, lit
from infra.jdbc import DataWarehouse, find_data, save_data
from infra.logger import get_logger
from infra.spark_session import get_spark_session
from infra.util import cal_std_day_yyyymmdd


class RoadDogTrasformer:
    @classmethod
    def transform(cls):
        for i in range(1, 21):
            road_dog_pd = pd.DataFrame(columns=['DESERTION_NO','COLOR','SEX','KIND_NM','AGE','WEIGHT' \
            ,'NEUTER_YN','PROCESS_STATE','HAPPEN_DT','HAPPEN_PLACE','SPECIAL_MARK','PROFILE','ST_CD', 'STD_DATE', 'NOTICE_DT'])

            road_dog_df = get_spark_session().createDataFrame(road_dog_pd \
                            , schema = 'DESERTION_NO string, COLOR string, SEX string, KIND_NM string, AGE string, WEIGHT string, NEUTER_YN string, PROCESS_STATE string, HAPPEN_DT string, HAPPEN_PLACE string, SPECIAL_MARK string, PROFILE string, ST_CD string, STD_DATE string, NOTICE_DT string')

            std_date=str(datetime.now().date()).replace('-','')
            shelter_df = find_data(DataWarehouse, 'SHELTER')
            path = '/roadpet/detail/road_dog_' + cal_std_day_yyyymmdd(1) + '.json'
            road_dog_json = get_spark_session().read.option("multiline","true").option("ignoreLeadingWhiteSpace","true").json(path, encoding='UTF-8').first()
            tmp = get_spark_session().createDataFrame(road_dog_json['response']['body']['items']['item'])
            road_dog_tmp = tmp.withColumn('KIND_NM', split(tmp['kindCd'], ' ', limit=2).getItem(1)) \
                                .withColumn('AGE', split(tmp['age'], '\\(', limit=2).getItem(0)) \
                                .withColumn('WEIGHT', split(tmp['weight'], '\\(', limit=2).getItem(0))
            # shelter_df.show()
            # road_dog_tmp.show()
            road_dog_shelter = road_dog_tmp.join(shelter_df, road_dog_tmp.careTel == shelter_df.CARE_TEL, how="left")
            # road_dog_tmp.show()

            road_dog_color = road_dog_shelter.withColumn("white", when(col('colorCd').rlike('^.*흰|백|(크림)|(화이트)|(아이보리)|(하양)|(하얀)|(백구)|희|(white).*'),"흰").otherwise(""))\
                                .withColumn("gold", when(col('colorCd').rlike('^.*(노랑)|(노란)|(누런)|(누렁)|황|금|(골드)|(베이지).*'), "금").otherwise(""))\
                                .withColumn("brown", when(col('colorCd').rlike('^.*갈|(브라운)|밤|(초코)|(고동)|(커피)|탄|(쵸코).*'), "갈").otherwise(""))\
                                .withColumn("grey", when(col('colorCd').rlike('^.*회|(실버)|(그레이).*'), "회").otherwise(""))\
                                .withColumn("black", when(col('colorCd').rlike('^.*검|흑|(블랙).*'), "검").otherwise(""))\
                                .withColumn("COLOR", concat('white','gold','brown','grey','black'))\
                                .withColumn("STD_DATE", lit(std_date))
            
            road_dog = road_dog_color.select(
                            col('desertionNo').alias('DESERTION_NO')
                            ,col('KIND_NM')
                            ,col('AGE')
                            ,col('WEIGHT')
                            ,col('COLOR')
                            ,col('ST_CD')
                            ,col('sexCd').alias('SEX')
                            ,col('neuterYn').alias('NEUTER_YN')
                            ,col('processState').alias('PROCESS_STATE')
                            ,col('happenDt').alias('HAPPEN_DT')
                            ,col('happenPlace').alias('HAPPEN_PLACE')
                            ,col('specialMark').alias('SPECIAL_MARK')
                            ,col('filename').alias('PROFILE')
                            ,col('STD_DATE')
                            ,col('noticeSdt').alias('NOTICE_DT'))

            road_dog_df = road_dog_df.unionByName(road_dog)
        road_dog_df.show()

        road_dog_today = road_dog_df.select("*").where(road_dog_df.NOTICE_DT==std_date)
        road_dog_today.show()

        road_dog_finish = road_dog_df.select("*").where(road_dog_df.PROCESS_STATE.like('종료%'))
        road_dog_finish.show()

