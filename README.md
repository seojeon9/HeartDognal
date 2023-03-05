<p align="left"><img src="https://user-images.githubusercontent.com/72624263/203254626-c6f1bc1a-53ae-4451-8cf3-07abe24d0616.png"> <br>
🏃 Data Engineer 손지수(팀장), 이상엽, 이서정 <br>
🏃 Data Scientist 김경현, 김태훈, 이지훈 <br>
🎈 Website https://heartdognal.ml/ <br>
🎈 Demo
<p align="left">
  <img src="https://user-images.githubusercontent.com/108858121/205203048-31fbcb78-38cd-4547-9e78-42fd8dfd5548.gif">
</p>

<br>

### **📖 Contents**  

1️⃣ [프로젝트 개요](#-프로젝트-개요)   
2️⃣ [데이터 파이프라인](#-데이터-파이프라인)  
3️⃣ [데이터 모델링](#-데이터-모델링)  
4️⃣ [기대효과 및 향후 계획](#-기대효과-및-향후-계획)    

<br>
  
## 🍎 프로젝트 개요


### ✔️ 프로젝트 기간  
2022-10-11~ 2022-11-17 (총 6주)

### ✔️ 주제 선정 배경 및 목적
> 국민 4분의 1정도가 반려동물을 키우는 지금. 그만큼 버려지는 동물들도 많습니다. 하루에만 평균 370마리가 버려지고 그의 절반 가량이 죽음을 맞이한다고 합니다. 현재의 입양률은 30%대로 저조하고 이마저도 파양을 당하는 경우가 부지기수입니다. <br>
> 그래서 저희는 입양희망자들이 나와 잘 맞는 아이는 어떤 특성을 가졌는지 파악하고 정보를 볼 수 있는 서비스를 기획하게 되었습니다. 

> 현재 운영되고 있는 유기견 서비스들은 정보 제공에 목적을 두고 있습니다. 국내에 몇 없는 매칭 서비스들은 품종을 추천하는 정도였습니다. 하지만 유기견의 80퍼센트 이상은 믹스견입니다. <br>
> 하트도그널은 품종견 뿐만 아니라 믹스견의 개별 특징을 파악해 입양희망자와 매칭 시키는 서비스를 만드는 것에 목적을 두고 있습니다.

### ✔️ 프로젝트 수행 도구

#### ETL Pipeline  
- 데이터 레이크 : <img src="https://img.shields.io/badge/Hadoop-66CCFF?style=flat-square&logo=ApacheHadoop&logoColor=white">  
- 데이터 웨어하우스, 데이터 마트, 운영 DB : <img src="https://img.shields.io/badge/Oracle-F80000?style=flat-square&logo=Oracle&logoColor=white">  
- 데이터 가공 및 분산 처리 엔진 : <img src="https://img.shields.io/badge/Spark-E25A1C?style=flat-square&logo=Apache Spark&logoColor=white">  
- 배치 도구 : <img src="https://img.shields.io/badge/Airflow-017CEE?style=flat-square&logo=Apache Airflow&logoColor=white"> <img  src="https://img.shields.io/badge/Oracle-F80000?style=flat-square&logo=Oracle&logoColor=white">  
- 로그 데이터 수집 : <img src="https://img.shields.io/badge/Kafka-231F20?style=flat-square&logo=Apache Kafka&logoColor=white">  
#### Web
  <img src="https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=HTML5&logoColor=white"> <img src="https://img.shields.io/badge/CSS-1572B6?style=flat-square&logo=css3&logoColor=white"> <img src="https://img.shields.io/badge/Javascript-F7DF1E?style=flat-square&logo=Javascript&logoColor=black"> <img src="https://img.shields.io/badge/Django-092E20?style=flat-square&logo=django&logoColor=white"> <img src="https://img.shields.io/badge/Bootstrap-7952B3?style=flat-square&logo=Bootstrap&logoColor=white">

#### Cowork Tools  
<img src="https://img.shields.io/badge/Trello-0052CC?style=flat-square&logo=Trello&logoColor=white">  https://trello.com/b/05Ro5oxL/heartdognal <br>
<img src="https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=Docker&logoColor=white">  docker pull zisu17/heartdognal:1.0 <br>
<img src="https://img.shields.io/badge/Slack-4A154B?style=flat-square&logo=Slack&logoColor=white"> <img src="https://img.shields.io/badge/Git-F05032?style=flat-square&logo=git&logoColor=white"> <br>

<br>

### ✔️ 워크플로우
  <p align="left"><img src="https://user-images.githubusercontent.com/72624263/203239444-7004e701-d069-454d-922c-0e24232ccb22.png" width="100%" height="100%"/>

### ✔️ 서비스 구성도
  <p align="left"><img src="https://user-images.githubusercontent.com/72624263/203254279-6382d614-4a70-47fc-a35c-9d936f64fed3.png" width="100%" height="100%"/>

<br>
<br>

## 🚀 데이터 파이프라인
### ✔️ 수집 데이터
  - 농림축산식품부 - 유기동물 API / 시도·시군구·보호소 API / 품종 API <br>
  - 네이버 견종정보 지식백과 크롤링 <br>
  - 사용자 로그 데이터

### ✔️ ERD
  - 데이터 웨어하우스 : 전사적인 측면에서 데이터를 수집하는 공간이기 때문에 데이터마트와 운영DB에 필요한 데이터들을 고려해 ERD를 구성했습니다  
  <p align="left"><img src="https://user-images.githubusercontent.com/72624263/203210993-06d79d64-5581-4ecd-b568-61884945099c.png" width="100%" height="100%"/>
  
  - 데이터마트 : 모델링에 필요한 유기견 데이터와 프로토타입 모델에서 필요한 지식백과 테이블을 가공하여 구성했습니다
  <p align="left"><img src="https://user-images.githubusercontent.com/72624263/203211130-ff89d313-40d0-4cb9-8ac3-4a0eec1be519.png" width="100%" height="100%"/>

  - 운영 DB : 유기견 테이블엔 군집화 라벨이 추가되고 그외엔 서비스에 필요한 시도 정보, 사용자 정보 그리고 사용자 활동 정보 테이블 등으로 구성되어 있습니다.
  <p align="left"><img src="https://user-images.githubusercontent.com/72624263/203211324-3b9232a9-42c6-402b-ba18-45f47be07303.png" width="100%" height="100%"/>

<br>

### ✔️ ETL
  - 지식백과 ETL : 지식백과 크롤링 후 가공

  <p align="left"><img src="https://user-images.githubusercontent.com/108858121/205209230-57f86e10-7d1d-42f8-b9e2-8508e2c3fc5a.png" width="100%" height="100%"/>
  <br>

  - 보호소 ETL : 보호소 API와 유기견 API의 관계를 활용하여 제공해주지 않는 정보를 찾아내 가공. 각 데이터의 전화번호로 조인하여 참조할 수 있도록 ID 부여

  <p align="left"><img src="https://user-images.githubusercontent.com/108858121/205065560-bff87d96-2148-4b8b-8850-575f73a5a932.png" width="100%" height="100%"/>
  <br>

  - 유기견 ETL : 유기견 API에서 추출 및 가공 후 배치 관리. 전화번호로 조인하여 보호소 ID 컬럼 생성

  <p align="left"><img src="https://user-images.githubusercontent.com/108858121/205078911-05d8ac1f-6e22-4100-8f15-b4dc8d292a93.png" width="100%" height="100%"/>
  <br>

<br>

### ✔️ 데이터 전처리
  - 색상 전처리 : 색상 컬럼을 불러와서 단어들을 구분하고 중복횟수가 10 이상인 단어들만 파악하여 색상 사전을 만듭니다. 색상 정보는 크게 흰, 갈, 검, 금, 회색으로 나눌 수 있습니다. 이렇게 색상 사전에 따라 단어가 분류되면 해당 색을 포함한 색상컬럼을 새로 만듭니다.

  <p align="left"><img src="https://user-images.githubusercontent.com/108858121/205209271-8b00dbff-cf37-4e45-a7a0-e02eaf4f8bd3.png" width="100%" height="100%"/>
  <br>
    
  - 특징 전처리 : 수집한 지식백과 데이터와 유기견 개별 특징의 단어들을 직접 비교해가며 특징 사전을 만들었습니다. 여기서 문제는 유기견 특징의 단어들이 사전에 있는 단어와 조금이라도 다르면 점수로 계산되지 않는다는 것에 있었습니다. 그래서 한국어 자연어 처리 모듈인 KoNLPy를 활용해 정형화를 하였습니다. 이 전처리로 평균 실루엣 점수 0.1을 증가시킬 수 있었습니다.

  <p align="center"><img src="https://user-images.githubusercontent.com/108858121/205209597-f030fe56-1c59-4d7c-924d-ab970f03a0f1.png" width="80%" height="80%"/>
  <br>

  - 모델링 전처리 : 비정형데이터인 강아지 특징 컬럼에서 친화성 정도와 건강상태를 수치화 하기 위해 특징 단어사전에서 친화성, 건강 관련 단어가 얼마나 매치되는지 개수를 세고, 매우 같은 강조 부사를 통해 가중치를 부여하여 친화성지수와 건강지수를 계산하였습니다.

  <p align="center"><img src="https://user-images.githubusercontent.com/108858121/205066704-62c147c6-9506-42e5-9804-e5231855b064.png" width="70%" height="70%"/>
  <br>

  - 이상치 전처리 : 이상치가 모델링 성능을 떨어뜨리기 때문에 체중과 나이 컬럼에서 이상치를 제거했습니다.

  <p align="center"><img src="https://user-images.githubusercontent.com/108858121/205069851-ebae098b-f1d1-4e1d-8f92-9f1a38fdaf1a.png" width="70%" height="70%"/>

<br>

### ✔️ 배치
  - Oracle scheduler : FINISHED_DOG(종료 유기견)과 비교하여 ROADDOG_INFO(모든 유기견)의 상태를 보호중에서 종료(반환/자연사/입양)로 업데이트 / 입양가능일로 부터 15일이 지난 경우 종료 처리하였습니다.

  <p align="left"><img src="https://user-images.githubusercontent.com/108858121/205072829-5ad3572b-2a7e-48d8-b02e-721416b71f8d.png" width="100%" height="100%"/>

  - Airflow : 매일 업데이트 되는 유기견 데이터를 수집 가공하고 군집화 모델을 거쳐 운영 DB에 밀어넣는 과정을 스케쥴링 했습니다. BashOperator로 Dag를 구성하여 파일별로 나눠져있는 각각의 task들을 하나의 파이프라인으로 동작할 수 있도록 구성했습니다.
    
  <p align="left"><img src="https://user-images.githubusercontent.com/108858121/222944890-3782c291-d5ed-4528-967c-564ed258285f.jpg" width="100%" height="100%"/>


<br>

### ✔️ 로그 데이터 수집
  - Kafka : Django 연동을 통해 Web에서 사용자 로그 데이터를 수집. HDFS에 로그 데이터 적재

  <p align="left"><img src="https://user-images.githubusercontent.com/108858121/205209073-ac0cd465-e293-4bd8-97b0-ef3639beb763.png" width="100%" height="100%"/>


<br>
<br>

## 🎯 데이터 모델링
### ✔️ 데이터 피처
  유기견 입양에 대한 인식조사 및 동물보호 국민의식조사를 보면 유기견 입양에 있어서 건강상태, 친화성 등 나이와 성격이 중요함을 알 수 있었고 유기견 입양확률예측모형 논문에서 성별 및 중성화여부 또한 유기견 입양에 있어서 중요함을 알 수 있었습니다.

  앞서 본 통계자료 및 논문을 바탕으로 유기견 입양에 있어 중요한 피쳐 7가지를 선별하였습니다.

  이 중 수치형 변수인 체중, 나이, 친화성, 건강상태는 군집화, 콘텐츠기반 필터링 추천시스템에 사용하였으며 명목형 변수인 품종, 성별, 중성화여부는 웹페이지에 정보가 제공될 수 있도록 활용하였습니다.

<br>

### ✔️ 클러스터링
  군집화는 입양희망자가 선호하는 반려견에 대한 설문조사를 바탕으로 해당하는 군집의 유기견을 추천해줄 수 있도록 모델링하였습니다.

  서비스 플로우에서 입양희망자는 로그인 후 설문조사를 통해 입양을 희망하는 강아지의 크기, 나이, 친화성정도, 건강상태 등을 설문조사하게됩니다. 설문조사 데이터를 바탕으로 해당 입양희망자에게 가장 잘 맞는 그룹의 유기견들이 선택되고 추천 페이지에는 선택된 유기견들이 보이게 됩니다.

  - K-Means : 군집의 개수가 11개에서 30개인 모델의 기준으로 K-Means는 평균 0.5이상의 비교적 높은 실루엣 점수를 보였으며 군집의 개수가 25개 이상일 시 군집의 데이터 및 실루엣 계수 분포 역시 비교적 고른 결과를 보였습니다.

  <p align="left"><img src="https://user-images.githubusercontent.com/108858121/205088612-aa933bc7-cc12-435d-b80d-a97cad28782f.png" width="100%" height="100%"/>

  - 가우시안 혼합모델 : 평균 실루엣 점수가 0.25에서 0.44정도로 K-Means에 비해 많이 낮았으며 특정 군집에 데이터가 편중되거나 실루엣 점수 분포가 고르지 못한 결과를 보였습니다.

  <p align="left"><img src="https://user-images.githubusercontent.com/108858121/205088689-d5de8a5b-03f0-46d9-ba24-8054f8b95100.png" width="100%" height="100%"/>

  - DBSCAN : 주요 하이퍼파라미터인 입실론과 min_samples에 따른 평균 실루엣 점수는 대부분 0.3 미만으로 K-Means와 가우시안 혼합모델에 비해 많이 낮은 결과를 보였습니다.

  <p align="left"><img src="https://user-images.githubusercontent.com/108858121/205088789-01794e73-3855-4cf6-8c6a-6c1eda64f29d.png" width="100%" height="100%"/>

  ▶ 최종 모델링 알고리즘 : K-Means

<br>

### ✔️ 하이퍼파라미터 튜닝
  K-Means의 가장 중요한 하이퍼파라미터인 클러스터링 개수를 정하는 것이 모델링의 핵심적인 부분이였고 모델링 성능 뿐만 아니라 서비스 차원의 문제도 고려해야 했습니다. 
  - 추천 강아지의 다양성 정도 : 추천 받는 강아지의 다양성을 높이려면 군집의 개수를 낮춰야되고, 설문조사에 정말 잘 맞는 강아지를 추천하려면 군집의 개수를 올려야되기 때문에 적절한 군집의 개수를 정하는 것이 중요하다고 볼 수 있겠습니다.
  - 입양 가능한 일일 평균 유기동물 수 : 입양이 가능한 강아지는 하루 주기로 업데이트 되며 일일 평균 2000마리에서 2500마리인 것으로 확인되었습니다. 저희는 추천서비스의 품질을 위해서 각 군집 1개당 평균 강아지 수 100마리 이상의 강아지가 필요하다고 판단하였으며 그에 따른 적절한 군집의 수는 20개에서 25개 이하로 판단하였습니다.

  - 엘보우 메소드와 실루엣 분석 : 엘보우 메소드는 군집의 개수가 17개 이상일 시 군집 내 변동성이 완만한 곡선 형태로 변화하며 실루엣 점수는 군집의 개수가 25개 이상일 시 0.5를 상회 하고 군집별 데이터 및 실루엣 계수 분포가 좋은 결과를 보였습니다.

  <p align="left"><img src="https://user-images.githubusercontent.com/108858121/205067134-9dadf065-a2f3-4645-b31e-43e69c782450.png" width="100%" height="100%"/>

  - 또 클러스터링 개수를 제외한 max_iter(최대 반복횟수), n_init(초기 중심위치 시도 횟수) 등의 하이퍼파라미터를 튜닝하였습니다. K-Means의 하이퍼파라미터 튜닝결과는 아래 보시는 표와 같습니다.
  <p align="left"><img src="https://user-images.githubusercontent.com/108858121/205067217-ead61799-8c8e-4063-ab65-cf6dee9d7aa5.png" width="100%" height="100%"/>


  ▶ 최종 클러스터링 개수 : 25개

<br>

### ✔️ 데이터 스케일링

  - 전체적으로 스탠다드 스케일이 다른 두 스케일러에 비해 높은 성능을 보였습니다.

  <p align="center"><img src="https://user-images.githubusercontent.com/72624263/203216112-b6b5b11e-8fbc-440e-85a4-825f9a726ba6.png" width="90%" height="90%"/>
 
<br>
<br>

  💥 최종 군집화 모델은 유기견 데이터 약 2만건에 대한 학습을 진행하였습니다.  
  
     알고리즘 : K-Means  
     데이터 스케일러 : Standard  
     하이퍼파라미터 : 상단의 표 참고  


  <br>

### ✔️ 콘텐츠 기반 필터링 추천 시스템
   - 설문조사를 바탕으로 추천된 군집의 유기견 중 한마리를 클릭하게 되면 코사인 유사도를 이용하여 만들어진 유기견 테이블에서 선택한 유기견과 유사한 강아지 5마리가 보여집니다.  
   - 군집화에 의한 추천과 콘텐츠 기반 필터링 추천의 차이점은 군집화는 특정 군집 안에서 추천이 이루어지지만 콘텐츠 필터링 추천시스템은 군집과 상관 없이 선택된 강아지와 유사도가 높은순으로 추천이 이루어지게 됩니다.

  <p align="center"><img src="https://user-images.githubusercontent.com/108858121/205084111-f9a4e631-7f3e-40fd-a513-06f6d329e299.png" width="100%" height="100%"/>


<br>
<br>

## 🍏 기대효과 및 향후 계획
### ✔️ 서비스 기대효과
  - 입양희망자가 원하는 유기견을 분석해 정보를 제공하고 잘 맞는 유기견을 매칭함으로써 유기견 파양률 줄일 수 있습니다. 또한 서비스를 이용하는 사람이 많아지면 입양 문화 활성화 효과를 기대할 수 있습니다. 

### ✔️ 향후 계획
  - 현재 저희의 데이터파이프라인은 결합도가 높습니다. 시스템 아키텍처의 결합도를 낮추기 위해 REST_API 서버와 Kafka를 이용해 데이터 파이프라인이 특정 서비스와 직접적으로 연결 되지 않도록 만들어 줄 예정입니다. 
  - 현재는 카프카가 웹 서비스와 연동되어 메시징 큐로서 로그를 수집하고 있습니다. 추후에는 수집된 로그로 테이블을 생성하여 분석 모델에 쓰일 수 있도록 데이터 파이프라인을 구축하겠습니다.
  - 추천의 다양성과 추천의 질을 높이기 위해 유기강아지 데이터 셋의 털 색상과 털 상태의 피처를 추가해 모델링하여 기존의 추천서비스와 비교하여 적용해볼 예정입니다.
  - 저희 서비스의 추천시스템 모델은 향후 일정 수 이상의 사용자 데이터 확보 시 콘텐츠 기반 추천시스템에서 콘텐츠 기반과 아이템 기반 협업 필터링이 결합된 하이브리드 추천시스템이 적용될 수 있도록 시스템을 구성할 계획입니다. 다수 사용자의 관심지수 데이터를 이용하여 사용자의 입양 선호도를 고려하고 더 폭 넓은 추천이 가능하게 될 것으로 예상됩니다.

<br>
