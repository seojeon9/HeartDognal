from infra.jdbc import DataWarehouse, OperateDatabase, find_data, save_data


class ShelterOpTrasformer:

    @classmethod
    def transform(cls):
        shelter_df = find_data(DataWarehouse, 'SHELTER')

        save_data(OperateDatabase, shelter_df, 'SHELTER')
