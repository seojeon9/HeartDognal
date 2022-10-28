from infra.hdfs_client import get_client
from infra.util import execute_rest_api


class KindExtract:
    URL = 'http://apis.data.go.kr/1543061/abandonmentPublicSrvc/kind'
    SERVICE_KEY = 'NJZf0IxXtTO8vlgpcZ8TbyYzgziNOLkFbn8dWmvTRbx4AYWTjdPnpNd2nbroAcineXLi971rvGbpoy23qSMPmQ=='
    FILE_DIR = '/road_pet/kind/'

    @classmethod
    def extract_data(cls):

        params = cls.__create_param()
        res = execute_rest_api('get', cls.URL, {}, params)
        file_name = 'kind.json'
        cls.__upload_to_hdfs(file_name, res)

    @classmethod
    def __upload_to_hdfs(cls, file_name, res):
        get_client().write(cls.FILE_DIR + file_name, res, encoding='utf-8', overwrite=True)

    @classmethod
    def __create_param(cls):
        return {
            'serviceKey': cls.SERVICE_KEY,
            'up_kind_cd': '417000',
            '_type': 'json'
        }
