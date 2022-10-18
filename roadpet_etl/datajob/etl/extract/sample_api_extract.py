import json
from multiprocessing import get_logger
from infra.hdfs_client import get_client
import urllib.request

from infra.jdbc import DataWarehouse, find_data
from infra.util import get_movie_codes


class NaverSearchMovieExtractor:

    URL = 'https://openapi.naver.com/v1/search/movie.json?query='
    CLIENT_ID = 'pOdfwRraC5W55dxPeRPQ'
    CLIENT_KEY = '8jQTYZWryv'
    FILE_DIR = '/movie/naver_search_movie/'

    movie_codes = []
    movie_names = []

    @classmethod
    def extract_data(cls):

        cls.movie_codes, cls.movie_names = get_movie_codes()

        for i in range(len(cls.movie_codes)):
            code = cls.movie_codes[i]
            name = cls.movie_names[i]

            params = cls.__create_param(name)

            response = cls.__get_never_search_api(name)
            rescode = response.getcode()

            cls.__upload_to_hdfs_from_response(code, params, response, rescode)

    @classmethod
    def __upload_to_hdfs_from_response(cls, code, params, response, rescode):
        try:
            if (rescode == 200):
                response_body = response.read()
                res = response_body.decode('utf-8')
                file_name = 'naver_search_movie_' + code + '.json'
                cls.__upload_to_hdfs(file_name, res)
            else:
                print("Error Code:" + rescode)
        except Exception as e:
            print('예외발생 : ', e)
            log_dict = cls.__create_log_dict(params)
            cls.__dump_log(log_dict, e)
            raise e

    @classmethod
    def __get_never_search_api(cls, name):
        encText = urllib.parse.quote(name)
        url = cls.URL + encText
        request = urllib.request.Request(url)
        request.add_header("X-Naver-Client-Id", cls.CLIENT_ID)
        request.add_header("X-Naver-Client-Secret", cls.CLIENT_KEY)
        response = urllib.request.urlopen(request)
        return response

    @classmethod
    def __create_param(cls, name):
        params = {
            'query': name
        }

        return params

    @classmethod
    def __upload_to_hdfs(cls, file_name, res):
        get_client().write(cls.FILE_DIR + file_name, res, encoding='utf-8', overwrite=True)

    @classmethod
    def __dump_log(cls, log_dict, e):
        log_dict['err_msg'] = e.__str__()
        log_json = json.dumps(log_dict, ensure_ascii=False)
        get_logger().error(log_json)
        # get_logger('naver_search_movie_extractor').error(log_json)

    @classmethod
    def __create_log_dict(cls, params):
        log_dict = {
            'is_success': 'Fail',
            'type': 'naver_search_movie',
            'params': params
        }

        return log_dict
