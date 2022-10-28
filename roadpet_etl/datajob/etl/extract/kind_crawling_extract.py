from urllib.request import urlopen
import bs4
import requests
import pandas as pd
import json
from infra.hdfs_client import get_client
from infra.logger import get_logger
from infra.spark_session import get_spark_session


class DogKindExtractor:
    file_dir = '/roadpet/dog/kind/'

    @classmethod
    def extract_data(cls):
        # url 추출
        url_li = []
        for i in range(1, 14):
            page_url = "https://terms.naver.com/list.naver?cid=42883&categoryId=44358&page=" + str(i)
            html = requests.get(page_url).content
            dog_url = bs4.BeautifulSoup(html, 'html.parser')
            info = dog_url.findAll('div', {'class': 'info_area'})

            for j in range(0, 15):
                url_base = 'https://terms.naver.com/'
                log_dict = {
                    "is_success": "Fail", "type": "dog_kind_extract", "page": str(i), "num_of_rows": str(j)
                }

                try:
                    link = info[j].find('a')['href']
                    url = url_base+link
                    url_li.append(url)

                except:
                    print(page_url)

        # 특징 추출
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.141 Whale/3.15.136.29 Safari/537.36"}

        # 빈 DataFrame 생성
        dog_kind = pd.DataFrame(columns=['품종', '원산지', '체고', '체중', '크기', '외모', '성격', '추천성향', '주요유의질병', '색상', '그룹구분', '친화성', '털빠짐', '집지키기', '실내외구분'])
        print(dog_kind)

        for url in url_li:
            res = requests.get(url, headers=headers)

            html = res.text
            bs_obj = bs4.BeautifulSoup(html, 'html.parser')

            품종 = bs_obj.select('h2')[1].text

            profile_list = bs_obj.find('div', {'class', 'tmp_profile'})

            if profile_list != None:
                pl_td = profile_list.select('td')

                원산지 = pl_td[0].text.strip()
                체고 = pl_td[1].text.strip()
                체중 = pl_td[2].text.strip()
                크기 = pl_td[3].text.strip()
                외모 = pl_td[4].text.strip()
                성격 = pl_td[5].text.strip()
                추천성향 = pl_td[6].text.replace(' ', '').replace('\n', '')

                if pl_td[7].select('a') == []:
                    주요유의질병 = ''

                    색상 = pl_td[7].text.strip()
                    그룹구분 = pl_td[8].text.strip().split(' ')[0]
                    친화성 = pl_td[9].text.strip()
                    if len(pl_td) == 13:
                        털빠짐 = pl_td[10].text.strip()
                        집지키기 = pl_td[11].text.strip()
                        실내외구분 = pl_td[12].text.strip()
                    else:
                        털빠짐 = ''
                        집지키기 = pl_td[10].text.strip()
                        실내외구분 = pl_td[11].text.strip()

                else:
                    주요유의질병 = pl_td[7].text.replace(' ', '').replace('\n', '')

                    색상 = pl_td[8].text.strip()
                    그룹구분 = pl_td[9].text.strip().split(' ')[0]
                    친화성 = pl_td[10].text.strip()
                    if len(pl_td) == 14:
                        털빠짐 = pl_td[11].text.strip()
                        집지키기 = pl_td[12].text.strip()
                        실내외구분 = pl_td[13].text.strip()
                    else:
                        털빠짐 = ''
                        집지키기 = pl_td[11].text.strip()
                        실내외구분 = pl_td[12].text.strip()

                dog_kind.loc[len(dog_kind)] = [품종, 원산지, 체고, 체중, 크기, 외모, 성격, 추천성향, 주요유의질병, 색상, 그룹구분, 친화성, 털빠짐, 집지키기, 실내외구분]


        print(dog_kind)
        # 스파크 형식으로 올리기
        dog_kind=get_spark_session().createDataFrame(dog_kind)
        # HDFS 올리는 코드 (밑에2개) 아래꺼는 나누지않은 그..... 스파크머시기
        # get_client().write(cls.file_dir + '지식백과특징.csv', dog_kind, encoding='CP949', overwrite=True) 
        dog_kind.coalesce(1).write.mode("overwrite").format("csv").option("header", "true").save("/roadpet/dog/kind/지식백과특징.csv")
