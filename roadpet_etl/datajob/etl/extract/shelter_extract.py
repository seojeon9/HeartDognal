import json
from infra.hdfs_client import get_client
from infra.jdbc import DataWarehouse, find_data
from infra.util import execute_rest_api
from infra.logger import get_logger


class ShelterExtract:
    URL = 'http://apis.data.go.kr/1543061/abandonmentPublicSrvc/shelter?'
    SERVICE_KEY = 'NJZf0IxXtTO8vlgpcZ8TbyYzgziNOLkFbn8dWmvTRbx4AYWTjdPnpNd2nbroAcineXLi971rvGbpoy23qSMPmQ=='
    FILE_DIR = '/road_pet/shelter/shelter/'

    @classmethod
    def extract_data(cls):

        sido_df = find_data(DataWarehouse, 'SIGUNGU')
        sido_df = sido_df.toPandas()
        for i in range(sido_df['SIDO_CD'].count()):
            sido = str(sido_df['SIDO_CD'][i])
            sigungu = str(sido_df['SIGUNGU_CD'][i])
            # print(i, '번:', sido, sigungu)
            # print(type(sido))

            try:
                params = cls.__create_param(sido, sigungu)
                res = execute_rest_api('get', cls.URL, {}, params)
                file_name = 'shelter_' + params['upr_cd'] + '_' + params['org_cd'] + '.json'
                cls.__upload_to_hdfs(file_name, res)
            except Exception as e:
                log_dict = cls.__create_log_dict(params)
                cls.__dump_log(log_dict, e)
                raise e

    @classmethod
    def __upload_to_hdfs(cls, file_name, res):
        get_client().write(cls.FILE_DIR + file_name, res, encoding='utf-8', overwrite=True)

    @classmethod
    def __create_param(cls, upr_cd, org_cd):
        return {
            'serviceKey': cls.SERVICE_KEY,
            'upr_cd': upr_cd,
            'org_cd': org_cd,
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
