from infra.jdbc import DataWarehouse, save_data
from infra.spark_session import get_spark_session


class SidoTrasformer:

    @classmethod
    def transform(cls):
        path = '/road_pet/shelter/sido/sido.json'
        sido_json = get_spark_session().read.option(
            "multiline", "true").json(path, encoding='UTF-8').first()

        sido_df = get_spark_session().createDataFrame(
            sido_json['response']['body']['items']['item'])

        # DW테이블에 맞게 가공
        # save_data(DataWarehouse, sido_df, 'ACTORS')
