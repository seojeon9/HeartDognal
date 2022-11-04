import json
from infra.hdfs_client import get_client
from infra.jdbc import DataWarehouse, find_data
from infra.spark_session import get_spark_session
from infra.util import execute_rest_api
from infra.logger import get_logger


class ShelterDetailExtract:
    URL = 'http://apis.data.go.kr/1543061/abandonmentPublicSrvc/abandonmentPublic?'
    SERVICE_KEY = 'NJZf0IxXtTO8vlgpcZ8TbyYzgziNOLkFbn8dWmvTRbx4AYWTjdPnpNd2nbroAcineXLi971rvGbpoy23qSMPmQ=='
    FILE_DIR = '/road_pet/shelter/shelter_detail/'

    @classmethod
    def extract_data(cls):
        sido_df = find_data(DataWarehouse, 'SIGUNGU')
        sido_df = sido_df.toPandas()
        shelter_list = []

        for i in range(sido_df['SIDO_CD'].count()):
            sido = str(sido_df['SIDO_CD'][i])
            sigungu = str(sido_df['SIGUNGU_CD'][i])

            shelter_df = cls.__generate_df(sido, sigungu)
            if shelter_df == '':
                print(sido, sigungu)
                continue

            print(sido, sigungu)
            shelter_df.show()
            shelter_df = shelter_df.toPandas()
            for shelter in shelter_df['careRegNo']:
                print(shelter)
                try:
                    params = cls.__create_param(shelter)
                    res = execute_rest_api('get', cls.URL, {}, params)
                    file_name = 'shelter_' + sido + '_' + sigungu + '_' + params['care_reg_no'] + '.json'
                    shelter_list.append(file_name)
                    cls.__upload_to_hdfs(file_name, res)
                except Exception as e:
                    log_dict = cls.__create_log_dict(params)
                    cls.__dump_log(log_dict, e)
                    raise e

        with open('shelter_file_list.txt', 'w', encoding='UTF-8') as f:
            for shelter in shelter_list:
                f.write(shelter+'\n')

    @classmethod
    def __upload_to_hdfs(cls, file_name, res):
        get_client().write(cls.FILE_DIR + file_name, res, encoding='utf-8', overwrite=True)

    @classmethod
    def __create_param(cls, care_reg_no):
        return {
            'serviceKey': cls.SERVICE_KEY,
            'upkind': '417000',
            'care_reg_no': care_reg_no,
            'numOfRows': '1',
            '_type': 'json',
        }

    @classmethod
    def __dump_log(cls, log_dict, e):
        log_dict['err_msg'] = e.__str__()
        log_json = json.dumps(log_dict, ensure_ascii=False)
        get_logger('shelter_extract').error(log_json)

    @classmethod
    def __create_log_dict(cls, params):
        log_dict = {
            'is_success': 'Fail',
            'type': 'shelter',
            'params': params
        }

        return log_dict

    @classmethod
    def __generate_df(cls, sido, sigungu):

        path = '/road_pet/shelter/shelter/shelter_' + sido + '_' + sigungu + '.json'
        shelter_json = get_spark_session().read.option("multiline", "true").json(path, encoding='UTF-8').first()

        try:
            shelter_df = get_spark_session().createDataFrame(shelter_json['response']['body']['items']['item'])
            return shelter_df

        except:
            return ''
