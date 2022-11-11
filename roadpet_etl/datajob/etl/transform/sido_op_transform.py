from infra.jdbc import DataWarehouse, OperateDatabase, find_data, save_data


class SidoOpTrasformer:

    @classmethod
    def transform(cls):
        sido_df = find_data(DataWarehouse, 'SIDO')

        save_data(OperateDatabase, sido_df, 'SIDO')
