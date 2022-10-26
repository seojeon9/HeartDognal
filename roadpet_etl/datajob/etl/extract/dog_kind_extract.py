from urllib.request import urlopen
import bs4
import requests
import pandas as pd
import json
from infra.logger import get_logger
from infra.hdfs_client import get_client
from infra.jdbc import DataWarehouse, find_data

class DogKindExtractor:
    file_dir = '/roadpet/dog/kind'
    
    @classmethod
    def extract_data(cls):
        url_li=[]
        for i in range(1,14):
            page_url="https://terms.naver.com/list.naver?cid=42883&categoryId=44358&page=" + str(i)
            html = requests.get(page_url).content
            dog_url = bs4.BeautifulSoup(html,'html.parser')
            info = dog_url.findAll('div',{'class':'info_area'})

            for j in range(0,15):
                url_base = 'https://terms.naver.com/'
                log_dict = {
                    "is_success":"Fail"
                    ,"type":"dog_kind_extract"
                    ,"page":str(i)
                    ,"num_of_rows":str(j)
                }

                try:
                    link = info[j].find('a')['href']
                    url = url_base+link
                    url_li.append(url)

                except Exception as e:
                    log_dict['err_msg']= e.__str__()
                    log_json = json.dumps(log_dict, ensure_ascii=False)
                    get_logger('dog_kind_extract').error(log_json)