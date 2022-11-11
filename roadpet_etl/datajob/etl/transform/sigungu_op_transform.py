from infra.jdbc import DataWarehouse, OperateDatabase, find_data, save_data


class SigunguOpTrasformer:

    @classmethod
    def transform(cls):
        sigungu_df = find_data(DataWarehouse, 'SIGUNGU')

        save_data(OperateDatabase, sigungu_df, 'SIGUNGU')
