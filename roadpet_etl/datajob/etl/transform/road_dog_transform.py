import json
from pyspark.sql.functions import split, col
from infra.jdbc import DataWarehouse, save_data
from infra.logger import get_logger
from infra.spark_session import get_spark_session
from infra.util import cal_std_day_yyyymmdd


class RoadDogTrasformer:
    @classmethod
    def transform(cls):
        for i in range(3, 1096):
            try:
                path = '/roadpet/detail/road_dog_' + cal_std_day_yyyymmdd(i) + '.json'
                road_dog_json = get_spark_session().read.option("multiline","true").option("ignoreLeadingWhiteSpace","true").json(path, encoding='UTF-8').first()
                tmp = get_spark_session().createDataFrame(road_dog_json['response']['body']['items']['item'])
                road_dog_df = tmp.withColumn('KIND_NM', split(tmp['kindCd'], ' ', limit=2).getItem(1)) \
                                        .withColumn('AGE', split(tmp['age'], '\\(', limit=2).getItem(0)) \
                                        .withColumn('WEIGHT', split(tmp['weight'], '\\(', limit=2).getItem(0))

                road_dog_select = road_dog_df.select(
                    col('desertionNo').alias('DESERTION_NO')
                    ,col('KIND_NM')
                    ,col('AGE')
                    ,col('WEIGHT')
                    ,col('neuterYn').alias('NEUTER_YN')
                    ,col('processState').alias('PROCESS_STATE')
                    ,col('happenDt').alias('HAPPEN_DT')
                    ,col('happenPlace').alias('HAPPEN_PLACE')
                    ,col('specialMark').alias('SPECIAL_MARK')
                    ,col('filename').alias('PROFILE'))
            
                save_data(DataWarehouse, road_dog_select, 'ROADDOG_INFO')
                
            except Exception as e:
                log_dict = {
                        "is_success":"Fail"
                        ,"type":"road_dog_transform"
                        ,"std_day":cal_std_day_yyyymmdd(i)
                    }
                log_dict['err_msg']= e.__str__()
                log_json = json.dumps(log_dict, ensure_ascii=False)
                get_logger('road_dog_transform').error(log_json)

