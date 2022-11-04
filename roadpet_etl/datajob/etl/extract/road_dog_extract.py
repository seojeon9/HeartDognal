import json
from infra.hdfs_client import get_client
from infra.logger import get_logger
from infra.util import cal_std_day_yyyymmdd, execute_rest_api

class RoadDogExtractor:
    url = 'http://apis.data.go.kr/1543061/abandonmentPublicSrvc/abandonmentPublic?'
    service_key = 'Trk0PUjGXkzmL99c4tVFWTwqQcElfON82T+zMvqwy1gy6G+TOz0Y1LWagIbe5xjXtWsSMXVhO92jGIsFoxChXA=='
    file_dir = '/roadpet/detail/'

    @classmethod
    def extract_data(cls, befor_cnt=40):
        
        for i in range(0, befor_cnt+1):
            params = cls.__create_param(i)

            try:
                res = execute_rest_api('get', cls.url, {}, params)
                file_name = 'road_dog_' + params['bgnde'] + '.json'
                cls.__upload_to_hdfs(res, file_name)

            except Exception as e:
                log_dict = cls.__create_log_dict(params)
                cls.__dump_log(e, log_dict)

    @classmethod
    def __dump_log(cls, e, log_dict):
        log_dict['err_msg']= e.__str__()
        log_json = json.dumps(log_dict, ensure_ascii=False)
        get_logger('road_dog_extractor').error(log_json)

    @classmethod
    def __create_log_dict(cls, params):
        return {
                "is_success":"Fail"
                ,"type":"road_dog_extract"
                ,"bgnde":params['bgnde']
                ,"params":params
            }

    @classmethod
    def __upload_to_hdfs(cls, res, file_name):
        return get_client().write(cls.file_dir + file_name, res, encoding='utf-8', overwrite=True)

    @classmethod
    def __create_param(cls, befor_day):
        return {
                'serviceKey':cls.service_key
                ,'bgnde':cal_std_day_yyyymmdd(befor_day)
                ,'endde':cal_std_day_yyyymmdd(befor_day)
                ,'upkind':'417000'
                ,'_type':'json'
                ,'numOfRows':'1000'
            }
