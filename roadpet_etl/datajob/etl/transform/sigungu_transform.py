from infra.jdbc import DataWarehouse, find_data, save_data
from infra.spark_session import get_spark_session


class SigunguTrasformer:

    @classmethod
    def transform(cls):
        # DW에서 시도 코드 받아오기
        sido_df = find_data(DataWarehouse, 'SIDO')
        # 디비에서 시도 읽어오기
        sido_list = sido_df[['SIDO_CD']].collect()

        for sido in sido_list:
            sigungu_df = cls.__generate_df(sido)
            if sigungu_df == '':
                print(sido)
                continue
            # DW의 테이블에 맞게 가공
            sigungu_df = sigungu_df.select(sigungu_df.orgCd.alias('SIGUNGU_CD'), sigungu_df.orgdownNm.alias('SIGUNGU_NM'), sigungu_df.uprCd.alias('SIDO_CD'))
            save_data(DataWarehouse, sigungu_df, 'SIGUNGU')

    @classmethod
    def __generate_df(cls, sido):
        sido = str(sido['SIDO_CD'])
        path = '/road_pet/shelter/sigungu/sigungu_' + sido + '.json'
        sigungu_json = get_spark_session().read.option("multiline", "true").json(path, encoding='UTF-8').first()
        try:
            sigungu_df = get_spark_session().createDataFrame(sigungu_json['response']['body']['items']['item'])
            return sigungu_df
        except:
            return ''
