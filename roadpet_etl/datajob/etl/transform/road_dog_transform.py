from datetime import datetime
import logging
import json
import pandas as pd
from pyspark.sql.functions import split, col, when, concat, lit
from datajob.etl.transform.module.clustering import create_model
from datajob.etl.transform.module.preprocessing import preprocess
from infra.jdbc import DataWarehouse, OperateDatabase, find_data, overwrite_data, save_data
import logging
from infra.spark_session import get_spark_session
from infra.util import cal_std_day_yyyymmdd

class RoadDogTrasformer:
    @classmethod
    def transform(cls):
        logging.getLogger().warn('>>>>>>>>>>>>>>>>>>> start')
    
        shelter_df = find_data(DataWarehouse, 'SHELTER')
        shelter_df = shelter_df.dropDuplicates(['CARE_ID'])
        road_dog_pd = pd.DataFrame(columns=['DESERTION_NO','COLOR_NM','SEX_CD','KIND_NM','AGE','WEIGHT','NEUTER_YN','PROCESS_ST','HAPPEN_DT','HAPPEN_PLACE','SPECIAL_MARK','THUMBNAIL','PROFILE', 'NOTICESDT', 'NOTICEEDT', 'CARE_ID', 'STD_DATE'])

        road_dog_df = get_spark_session().createDataFrame(road_dog_pd \
                        , schema = 'DESERTION_NO string, COLOR_NM string, SEX_CD string, KIND_NM string, AGE string, WEIGHT string, NEUTER_YN string, PROCESS_ST string, HAPPEN_DT string, HAPPEN_PLACE string, SPECIAL_MARK string, THUMBNAIL string, PROFILE string, NOTICESDT string, NOTICEEDT string, CARE_ID integer, STD_DATE string')
        logging.getLogger().warn('>>>>>>>>>>>>>>>>>>> df create1')
        for i in range(15, 16):
            std_date=str(datetime.now().date()).replace('-','')

            path = '/roadpet/detail/road_dog_' + cal_std_day_yyyymmdd(i) + '.json'
            road_dog_json = get_spark_session().read.option("multiline","true").json(path, encoding='UTF-8').first()
            tmp = get_spark_session().createDataFrame(road_dog_json['response']['body']['items']['item'])
            road_dog_tmp = tmp.withColumn('KIND_NM', split(tmp['kindCd'], ' ', limit=2).getItem(1)) \
                                .withColumn('AGE', split(tmp['age'], '\\(', limit=2).getItem(0)) \
                                .withColumn('WEIGHT', split(tmp['weight'], '\\(', limit=2).getItem(0))

            road_dog_shelter = road_dog_tmp.join(shelter_df, road_dog_tmp.careTel == shelter_df.CARE_TEL)

            road_dog_color = road_dog_shelter.withColumn("white", when(col('colorCd').rlike('^.*흰|백|(크림)|(화이트)|(아이보리)|(하양)|(하얀)|(백구)|희|(white).*'),"흰").otherwise(""))\
                                .withColumn("gold", when(col('colorCd').rlike('^.*(노랑)|(노란)|(누런)|(누렁)|황|금|(골드)|(베이지).*'), "금").otherwise(""))\
                                .withColumn("brown", when(col('colorCd').rlike('^.*갈|(브라운)|밤|(초코)|(고동)|(커피)|탄|(쵸코).*'), "갈").otherwise(""))\
                                .withColumn("grey", when(col('colorCd').rlike('^.*회|(실버)|(그레이).*'), "회").otherwise(""))\
                                .withColumn("black", when(col('colorCd').rlike('^.*검|흑|(블랙).*'), "검").otherwise(""))\
                                .withColumn("COLOR_TMP", concat('white','gold','brown','grey','black'))\
                                .withColumn("COLOR_NM", when(col("COLOR_TMP")=="", "기타").otherwise(col("COLOR_TMP")))\
                                .withColumn("STD_DATE", lit(std_date))
            
            road_dog = road_dog_color.select(
                            col('desertionNo').alias('DESERTION_NO')
                            ,col('KIND_NM')
                            ,col('AGE')
                            ,col('WEIGHT')
                            ,col('COLOR_NM')
                            ,col('CARE_ID')
                            ,col('sexCd').alias('SEX_CD')
                            ,col('neuterYn').alias('NEUTER_YN')
                            ,col('processState').alias('PROCESS_ST')
                            ,col('happenDt').alias('HAPPEN_DT')
                            ,col('happenPlace').alias('HAPPEN_PLACE')
                            ,col('specialMark').alias('SPECIAL_MARK')
                            ,col('filename').alias('THUMBNAIL')
                            ,col('popfile').alias('PROFILE')
                            ,col('noticeSdt').alias('NOTICESDT')
                            ,col('noticeEdt').alias('NOTICEEDT')
                            ,col('STD_DATE'))

            road_dog_df = road_dog_df.unionByName(road_dog)
        print(road_dog_df.count())

        road_dog_rename = road_dog_df.select(
                col('DESERTION_NO').alias('유기번호')
                ,col('AGE').alias('나이')
                ,col('WEIGHT').alias('체중')
                ,col('COLOR_NM').alias('색상')
                ,col('SPECIAL_MARK').alias('특징')
            )
        print('ds df rename')
        logging.getLogger().warn('>>>>>>>>>>>>>>>>>>> road_dog_rename.toPandas start')
        road_dog_rename = road_dog_rename.toPandas()
        logging.getLogger().warn('>>>>>>>>>>>>>>>>>>> road_dog_rename.toPandas end')
        # road_dog_rename = road_dog_rename.iloc[0:10,:]
        # road_dog_rename.to_csv('./datajob/etl/data/raw_data.csv',encoding = 'utf-8', index = False)

        # road_dog_today = road_dog_df.select("*").where(road_dog_df.NOTICE_DT==std_date)

        # road_dog_finish = road_dog_df.select("*").where(road_dog_df.PROCESS_STATE.like('종료%'))

        # ds쪽에서 만들어준 모델함수 호출 => 유기번호, 군집라벨
        # 스파크 데이터프레임으로 변환
        # 기존 데이터프레임과  변환한 데이터프레임을 유기번호로 조인
        # 거기서 운영디비에 필요한 컬럼만 셀랙트해서 새로운 데프로 바꾼다음 운영디비에 저장
        # data = pd.read_csv('/home/big/study/roadpet_etl/datajob/etl/data/raw_data.csv')
        pre_data = preprocess(road_dog_rename)
        logging.getLogger().warn('>>>>>>>>>>>>>>>>>>> pre_data')
        label_data = create_model(pre_data)
        label_data.columns = ['DESERTION_NO', 'LABEL']

        logging.getLogger().warn('>>>>>>>>>>>>>>>>>>> get_spark_session')
        label_data = get_spark_session().createDataFrame(label_data, schema='DESERTION_NO string, LABEL string')

        logging.getLogger().warn('>>>>>>>>>>>>>>>>>>> get_spark_session')

        label_data.show()

        road_dog_op = road_dog_df.join(label_data, road_dog_df.DESERTION_NO == label_data.DESERTION_NO, how='left').select(road_dog_df.DESERTION_NO, road_dog_df.KIND_NM,road_dog_df.AGE,road_dog_df.WEIGHT,road_dog_df.COLOR_NM,road_dog_df.CARE_ID,road_dog_df.SEX_CD,road_dog_df.NEUTER_YN,road_dog_df.PROCESS_ST,road_dog_df.HAPPEN_DT,road_dog_df.HAPPEN_PLACE,road_dog_df.SPECIAL_MARK,road_dog_df.THUMBNAIL,road_dog_df.PROFILE,road_dog_df.NOTICEEDT,road_dog_df.STD_DATE,label_data.LABEL)

        road_dog_df = road_dog_df.dropDuplicates(['DESERTION_NO'])
        road_dog_op = road_dog_op.dropDuplicates(['DESERTION_NO'])

        #save_data(DataWarehouse, road_dog_df, 'ROADDOG_INFO')
        save_data(OperateDatabase, road_dog_op, 'ROADDOG_INFO')

        


