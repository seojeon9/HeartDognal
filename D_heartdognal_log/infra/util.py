from datetime import datetime, timedelta
import requests

def cal_std_day(befor_day):   
    x = datetime.now() - timedelta(befor_day)
    year = x.year
    month = x.month if x.month >= 10 else '0'+ str(x.month)
    day = x.day if x.day >= 10 else '0'+ str(x.day)  
    return str(year)+ '-' +str(month)+ '-' +str(day)


def execute_rest_api(method, url, headers, params):    
    if method == 'get':
        res = requests.get(url, params=params, headers=headers)
    elif method == 'post':
        res = requests.post(url, params=params, headers=headers)
    
    if res is None or res.status_code != 200:
        raise Exception('응답코드 : ' + str(res.status_code))

    return res.text