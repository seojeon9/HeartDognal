from pyspark.sql.functions import col
from infra.jdbc import DataWarehouse, save_data
from infra.spark_session import get_spark_session
from infra.util import cal_std_day


class CoronaPatientTrasformer:

    @classmethod
    def transform(cls):
        path = '/corona_data/patient/corona_patient_' + \
            cal_std_day(1) + '.json'
        co_patient_json = get_spark_session().read.json(path, encoding='UTF-8')

        # 코로나 감염자 데이터
        data = cls.__crawling_corona_patients(co_patient_json)
        patient_data = get_spark_session().createDataFrame(data)
        co_patients = cls.__generate_data(patient_data)
        save_data(DataWarehouse, co_patients, 'CORONA_PATIENTS')

    @classmethod
    def __generate_data(cls, patient_data):
        co_patients = patient_data.select(
            patient_data.gubun.alias('LOC'), patient_data.deathCnt.alias('DEATH_CNT'), patient_data.defCnt.alias(
                'DEF_CNT'), patient_data.localOccCnt.alias('LOC_OCC_CNT'), patient_data.qurRate.alias('QUR_RATE'), patient_data.stdDay.alias('STD_DAY')
        ).where(~(col('LOC').isin(['합계', '검역']))).distinct()
        co_patients.printSchema()
        return co_patients

    @classmethod
    def __crawling_corona_patients(cls, co_patient_json):
        data = []
        for r1 in co_patient_json.select('items').toLocalIterator():
            if not r1.items:
                continue
            for r2 in r1.items:
                data.append(r2)
        return data
