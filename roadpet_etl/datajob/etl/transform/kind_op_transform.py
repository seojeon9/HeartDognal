from infra.jdbc import DataWarehouse, OperateDatabase, save_data
from infra.spark_session import get_spark_session


class KindOpTrasformer:

    @classmethod
    def transform(cls):
        path = '/road_pet/dog/kind/kind.json'
        kind_json = get_spark_session().read.option(
            "multiline", "true").json(path, encoding='UTF-8').first()

        kind_df = get_spark_session().createDataFrame(
            kind_json['response']['body']['items']['item'])

        kind_df = kind_df.select(kind_df.kindCd.alias(
            'KIND_CD'), kind_df.knm.alias('KIND_NM'))
        save_data(OperateDatabase, kind_df, 'KIND')
