from infra.jdbc import DataMart, DataWarehouse, find_data, save_data
from pyspark.sql.functions import col, ceil


class CoVaccine:

    @classmethod
    def save(cls):
        vaccine = find_data(DataWarehouse, 'CORONA_VACCINE')
        popu = find_data(DataWarehouse, 'loc')
        patients = find_data(DataWarehouse, 'corona_patients')

        tmp = cls.__pivot_vaccin_df(vaccine)
        vac_rate = cls.__calc_vac_rate(tmp, popu, patients)
        vac_rate.show(3)
        save_data(DataMart, vac_rate, 'CO_VACCINE')

    @classmethod
    def __calc_vac_rate(cls, tmp, popu, patients):
        vac_rate = tmp.join(popu, on='LOC') \
            .join(patients, on='LOC') \
            .select('LOC', patients.STD_DAY, ceil(col('v1')/col('population') * 100).alias('V1TH_RATE'), ceil(col('v2')/col('population') * 100).alias('V2TH_RATE'), ceil(col('v3')/col('population') * 100).alias('V3TH_RATE'), ceil(col('v4')/col('population') * 100).alias('V4TH_RATE'), 'QUR_RATE'
                    )

        return vac_rate

    @classmethod
    def __pivot_vaccin_df(cls, vaccine):
        pd_vaccine = vaccine.to_pandas_on_spark()
        pd_vaccine = pd_vaccine.pivot_table(
            index=['LOC', 'STD_DAY'], columns='V_TH', values='V_CNT')
        pd_vaccine = pd_vaccine.reset_index()
        tmp = pd_vaccine.to_spark()
        return tmp
