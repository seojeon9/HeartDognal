import random
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .models import AdoptionInquiry, Kind, RoaddogInfo, Sido, Survey, Shelter
from .module import kmeans_recom
from .module import content_recom
from sklearn.cluster import KMeans
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import joblib
from django.urls import reverse
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


def index(request):

    return render(request, 'accounts/index.html')


def about_us(request):
    return render(request, 'roaddog/about_us.html')


def recommend(request):
    # print('')
    # 1. 사용자가 전달한 별점 점수 가져오기
    # 2. 별점점수를 군집화 모듈로 전송(함수호출)
    # 3. 군집화모듈에서 군집레이블 결정후 몇번 레이블인지 반환
    # 4. 반환된 레이블과 같은 군집의 강아지 정보를 파일이나 디비에서 얻어오기
    # 5. 동일 군집 강아지 중 랜덤하게 선택
    # 6. 디비에서 선택된 강아지 세부 정보 추출
    # 7. 추출된 정보를 템플릿으로 전송

    #######################################
    # db에서 해당 라벨의 강아지 중 랜덤 3개 가져와서 보여주기

    # roaddog = list(RoaddogInfo.objects.filter(label=0).values())
    # random_roaddog = random.sample(roaddog, 3)
    # content = {'roaddog': random_roaddog}
    # print(content)
    # for i in range(len(random_roaddog)):
    #     content['roaddog'][i]['age'] = 2022 - int(content['roaddog'][i]['age'])
    return render(request, 'roaddog/recommend.html')


def presurvey(request):

    return render(request, 'roaddog/presurvey.html')


def search(request):
    sidos = Sido.objects.values()
    kinds = Kind.objects.values().order_by('kind_nm')
    roaddog = RoaddogInfo.objects.filter(process_st='보호중').values()
    content = {'sidos': sidos,
               'kinds': kinds,
               'roaddogs': roaddog}
    # print(content)
    return render(request, 'roaddog/search.html', content)


def search_filter(request):
    sido = request.GET['sido']
    kind = request.GET['kind']
    print('sido:'+sido+'kind:'+kind)
    # 쿼리문
    # SIGUNGU의 SIDO_CD = sido의 SIGUNGU_CD
    # SHLETER의 SIGUNGU_CD의 CARE_ID
    # ROADDOG_INFO의 CARE_ID
    # &
    # ROADDOB_INFO의 KIND_NM = kind
    if sido != '':
        if kind != '':
            roaddog = RoaddogInfo.objects.raw(
                'SELECT * FROM roaddog_info WHERE process_st= %s AND care_id IN (SELECT care_id FROM shelter WHERE sigungu_cd IN (SELECT sigungu_cd FROM sigungu WHERE sido_cd = %s)) INTERSECT SELECT * FROM roaddog_info WHERE kind_nm = %s;', ['보호중', sido, kind])
        else:
            roaddog = RoaddogInfo.objects.raw(
                'SELECT * FROM roaddog_info WHERE process_st= %s AND care_id IN (SELECT care_id FROM shelter WHERE sigungu_cd IN (SELECT sigungu_cd FROM sigungu WHERE sido_cd = %s))', ['보호중', sido])
    elif kind != '':
        roaddog = RoaddogInfo.objects.raw(
            'SELECT * FROM roaddog_info WHERE kind_nm = %s AND process_st= %s;', [kind, '보호중'])
    else:
        roaddog = RoaddogInfo.objects.filter(process_st='보호중').values()

    print(roaddog)
    sidos = Sido.objects.values()
    kinds = Kind.objects.values().order_by('kind_nm')
    content = {'sidos': sidos,
               'kinds': kinds,
               'roaddogs': roaddog
               }
    # print(content)
    return render(request, 'roaddog/search.html', content)


def survey(request):

    if request.method == 'GET':
        print('get request')
        return render(request, 'roaddog/survey.html')

    user = request.user
    weight = request.POST['weight']
    age = request.POST['age']
    friendly = request.POST['friendly']
    health = request.POST['health']

    survey = Survey.objects.filter(username=user)

    if not survey:
        survey = Survey(username=user.username, weight_cd=weight,
                        age_cd=age, health_cd=health, attr_cd=friendly)
        survey.save()
    else:
        survey = survey[0]

        survey.weight_cd = weight
        survey.age_cd = age
        survey.attr_cd = friendly
        survey.health_cd = health

        survey.save()

    age = list(Survey.objects.filter(username=user).values())[0]['age_cd']
    weight = list(Survey.objects.filter(
        username=user).values())[0]['weight_cd']
    health = list(Survey.objects.filter(
        username=user).values())[0]['health_cd']
    friendly = list(Survey.objects.filter(
        username=user).values())[0]['attr_cd']
    user_stars = np.array([[age, weight, health, friendly]])
    cluster_label = kmeans_recom.recommend(user_stars)
    print(cluster_label)
    roaddog = list(RoaddogInfo.objects.filter(
        label=cluster_label, process_st='보호중').values())

    dog_len = len(roaddog)
    print('라벨 강아지 마리수:', dog_len)
    if dog_len == 0:
        print('라벨강아지 0')
        roaddog = list(RoaddogInfo.objects.filter(process_st='보호중').values())
    elif dog_len < 3:
        print('라벨강아지 3미만')
        roaddog_null = list(RoaddogInfo.objects.filter(
            process_st='보호중').values())
        roaddog.append(random.sample(roaddog_null, 3-dog_len))

    random_roaddog = random.sample(roaddog, 3)

    content = {'roaddog': random_roaddog}
    print(content)

    for i in range(len(random_roaddog)):
        content['roaddog'][i]['age'] = 2022 - int(content['roaddog'][i]['age'])

    return render(request, 'roaddog/recommend.html', content)


def detail_info(request, desertion_num):
    # 선택된 강아지 아이디 얻어오기
    # 디비에서 해당 아이디 강아지 상세정보 가져오기
    # 유사도 테이블에서 선택된 강아지와 유사도가 놑은 강아지 아이디 찾기
    # 디비에서 유사도가 높은 강아지들 정보 얻어오기(10개) - 상세페이지 넘어가게
    # 템플릿에 강아지 정보 전송
    selected_dog = list(RoaddogInfo.objects.filter(
        desertion_no=desertion_num).values())

    sim10_reg_list = content_recom.recommend(desertion_num)
    top5_list = sim10_reg_list[:5]
    recom_dog = list(RoaddogInfo.objects.filter(
        Q(desertion_no=top5_list[0]) | Q(desertion_no=top5_list[1]) | Q(desertion_no=top5_list[2]) | Q(desertion_no=top5_list[3]) | Q(desertion_no=top5_list[4])).values())

    # print(recom_dog)
    selected_dog[0]['age'] = 2022 - \
        int(selected_dog[0]['age'])

    careid = selected_dog[0]['care_id']
    carenm = list(Shelter.objects.filter(
        care_id=careid).values())[0]['care_nm']
    selected_dog[0]['care_id'] = carenm

    shelter = Shelter.objects.filter(
        care_id=careid).values()[0]

    # print(shelter)
    for i in range(len(recom_dog)):
        recom_dog[i]['age'] = 2022 - int(recom_dog[i]['age'])

        careid = recom_dog[i]['care_id']
        carenm = list(Shelter.objects.filter(
            care_id=careid).values())[0]['care_nm']

        recom_dog[i]['care_id'] = carenm

    content = {'selected_dog': selected_dog,
               'recom_dog': recom_dog, 'shelter': shelter}

    return render(request, 'roaddog/detail_info.html', content)


@csrf_exempt
def adoption_inquiry(request):
    user = request.user
    desertion_no = request.POST['desertion_no']

    adop = AdoptionInquiry(username=user.username, desertion_no=desertion_no)
    adop.save()

    print('adoption_inquiry')
    # db에만 넣고 페이지적으로는 아무런 반환도 하고싶지 않음
    return JsonResponse()
