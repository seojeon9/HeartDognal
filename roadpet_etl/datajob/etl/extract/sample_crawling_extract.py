import time
from bs4 import BeautifulSoup
import requests
from datetime import datetime
import json
from infra.hdfs_client import get_client
from infra.jdbc import DataWarehouse, find_data

class MovieScoreExtractor:
    std_date=str(datetime.now().date())
    file_dir = '/movie/score/'
    cols = ['movie_code', 'title','audi_sc', 'expe_sc', 'neti_sc', 'std_date']

    @classmethod
    def extract_data(cls):
        
        movie_url_df = find_data(DataWarehouse, 'MOVIE_URL')
        movie_url_df = movie_url_df.toPandas()

        print(movie_url_df['MOVIE_CODE'])
        for i in range(len(movie_url_df['MOVIE_CODE'])):
            try : 
                data=[]
                file_name = 'movie_score_' + str(movie_url_df['MOVIE_CODE'][i]) + '_' + cls.std_date + '.json'
                url = movie_url_df['URL'][i]
                html = requests.get(url).content
                soup = BeautifulSoup(html,"html.parser")

                rows=[]
                rows.append(movie_url_df['MOVIE_CODE'][i])

                try :
                    title=soup.findAll("h3",{"class":"h_movie"})[0].text.split('\n')[1]
                    time.sleep(2)
                    rows.append(title)
                except Exception as e:
                    rows.append('없음')
                    
                    
                try :
                    audi_sc=soup.findAll("span",{"class":"st_on"})
                    time.sleep(1)
                    audi_sc=audi_sc[0].text.split(" ")[2].replace('점',"")
                    time.sleep(2)
                    rows.append(audi_sc)
                except Exception as e:
                    rows.append('없음')
                    
                    
                try :
                    expe_sc=soup.findAll("div",{"class":"spc_score_area"})
                    time.sleep(1)
                    expe_sc=expe_sc[0].text.split("\n\n")[2]
                    time.sleep(2)
                    rows.append(expe_sc)
                except Exception as e:
                    rows.append('없음')
                
                
                try :
                    neti_sc=soup.findAll("a",{"id":"pointNetizenPersentBasic"})
                    time.sleep(1)
                    neti_sc=neti_sc[0].text
                    time.sleep(2)
                    rows.append(neti_sc)
                except Exception as e:
                    rows.append('없음')
                
                rows.append(cls.std_date)
                
                tmp = dict(zip(cls.cols, rows))
                data.append(tmp)

                res = {
                    'meta':{
                        'desc':'네이버 영화 평점 현황',
                        'cols':{
                            'movie_code':'영화코드'
                            ,'title':'영화제목'
                            ,'audi_sc':'관람객평점'
                            ,'expe_sc':'기자및평론가평점'
                            ,'neti_sc':'네티즌평점'
                            ,'std_date':'수집일자'
                        },
                    },
                'data':data
                }

                get_client().write(cls.file_dir+file_name, json.dumps(res, ensure_ascii=False), encoding='utf-8', overwrite=True)
            except : 
                print('error')