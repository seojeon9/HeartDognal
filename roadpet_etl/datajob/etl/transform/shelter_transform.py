from infra.jdbc import DataWarehouse, save_data
from infra.spark_session import get_spark_session
import pandas as pd
from pyspark.sql.functions import lit, monotonically_increasing_id
from geopy.geocoders import Nominatim
geo_local = Nominatim(user_agent='South Korea')


class ShelterTrasformer:

    @classmethod
    def transform(cls):
        file = open('shelter_file_list.txt', 'r', encoding='UTF-8')
        path_list = file.readlines()
        print(path_list)
        file.close()

        for path in path_list:

            sigungu = path.split('_')[2]
            shelter = path.split('_')[3].split('.')[0]
            path = "/road_pet/shelter/shelter_detail/" + path.strip()
            shelter_df = cls.__generate_df(path)
            if shelter_df == ' ':
                continue
            # shelter_df.show()

            shelter_df = shelter_df.select(shelter_df.careAddr, shelter_df.careNm, shelter_df.careTel)
            addr = shelter_df.head()['careAddr'].split('(')[0]
            latitude, longitude = cls.__geocoding(addr)
            print(addr, latitude, longitude)
            shelter_df = shelter_df.withColumn('SIGUNGU_CD', lit(sigungu)).withColumn('ST_CD', lit(shelter)).withColumn('LATITUDE', lit(latitude)).withColumn(
                'LONGITUDE', lit(longitude)).withColumnRenamed('careAddr', 'ADDR_DETAIL').withColumnRenamed('careNm', 'CARE_NM').withColumnRenamed('careTel', 'CARE_TEL')

            save_data(DataWarehouse, shelter_df, 'SHELTER')

    @classmethod
    def __geocoding(cls, address):
        try:
            geo = geo_local.geocode(address)
            x_y = (geo.latitude, geo.longitude)
            return x_y
        except:
            return (0, 0)

    @classmethod
    def __generate_df(cls, path):
        try:
            shelter_json = get_spark_session().read.option("multiline", "true").json(path, encoding='UTF-8').first()
            shelter_df = get_spark_session().createDataFrame(shelter_json['response']['body']['items']['item'])
            return shelter_df
        except:
            return ' '

        # save_data(DataWarehouse, sigungu_df, 'ACTORS')
