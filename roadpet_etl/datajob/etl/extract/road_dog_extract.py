import json
from infra.hdfs_client import get_client
from infra.logger import get_logger
from infra.util import cal_std_day_yyyymmdd, execute_rest_api

class RoadDogExtractor:
    url = 'http://apis.data.go.kr/1543061/abandonmentPublicSrvc/abandonmentPublic?'
    service_key = 'Trk0PUjGXkzmL99c4tVFWTwqQcElfON82T+zMvqwy1gy6G+TOz0Y1LWagIbe5xjXtWsSMXVhO92jGIsFoxChXA=='
    file_dir = '/roadpet/detail/'

    @classmethod
    def extract_data(cls, befor_cnt=1090):
        
        for i in range(1, befor_cnt+1):
            params = {
                'serviceKey':cls.service_key
                ,'bgnde':cal_std_day_yyyymmdd(i)
                ,'endde':cal_std_day_yyyymmdd(i)
                ,'upkind':'417000'
                ,'_type':'json'
                ,'numOfRows':'1000'
            }

            log_dict = {
                "is_success":"Fail"
                ,"type":"road_dog_extract"
                ,"bgnde":params['bgnde']
                ,"params":params
            }

            try:
                res = execute_rest_api('get', cls.url, {}, params)
                file_name = 'road_dog_' + params['bgnde'] + '.json'
                get_client().write(cls.file_dir + file_name, res, encoding='utf-8', overwrite=True)

            except Exception as e:
                log_dict['err_msg']= e.__str__()
                log_json = json.dumps(log_dict, ensure_ascii=False)
                get_logger('road_dog_extractor').error(log_json)
