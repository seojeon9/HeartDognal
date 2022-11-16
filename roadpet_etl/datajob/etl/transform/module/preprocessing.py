import pandas as pd
import re
import numpy as np
from itertools import product
from konlpy.tag import Kkma
from konlpy.utils import pprint
from tqdm import tqdm_notebook
import logging

def preprocess(animal) :

    # 나이 형식에 안맞는 값 제거
    logging.getLogger().warn('>>>>>>>>>>>>>>>>>>> preprocess')
    animal['나이'] = animal['나이'].astype('str')
    p = re.compile('(\d){4}')

    drop_list = []
    for index, a in enumerate(animal['나이']):

        if p.search(a) == None:
            drop_list.append(index)

    animal = animal.drop(drop_list, axis=0)
    animal.reset_index(inplace=True)

    # ### 체중 이상한 값 제거

    animal['체중']=animal['체중'].astype('str')

    p = re.compile('\d*\.?\d+')

    drop_list = []
    for index, a in enumerate(animal['체중']) :

        if len(p.findall(a)) != 1 :
            drop_list.append(index)

    animal = animal.drop(drop_list, axis = 0)
    animal.reset_index(inplace=True)


    # ## konlpy

    animal['특징'] = animal['특징'].astype('str')

    kkma = Kkma()

    special_list = []

    for i in tqdm_notebook(range(len(animal))):
        if animal['특징'][i].replace(' ','') == '':
            special_list.append('')
        else:
            pos_character = kkma.pos(animal['특징'][i])
            word_list = []

        # print('a')
            for pos in pos_character:
                if pos[1] in ['NR','NNM','XR','NNG','NNP', 'VV', 'VA', 'MAG', 'VXV', 'VXA', 'VCN']:    # 'XSN','XSV', 'XSA' 파생접미사(~하다)
                    word_list.append(pos[0])

            word = " ".join(word_list)
            print(word)
            special_list.append(word)

    animal['특징'] = special_list


    # ## 건강 -

    # ### 1) 질병


    diseases = ['감염','염증','피부염','피부병','병변','외이염','내이염','결막염','질병','질환','종양','농피증','백내장','디스템퍼','폐렴','부종','곰팡이','개선충','진드기','안충','회충','기생충','사상충']


    # ### 2) 장애


    disorders1 = ['장애','골절','절단','사고','상해','탈구','탈골','탈장','기형','실명','절음','마비','괴사','허니아','부정교합']

    disorders2 = []
    for ite in list(product(*[['기립','보행','의식','걷'],['불가','불능','없','이상','불편']])) :
        disorders2.append(" ".join(ite))

    disorders3 = []
    for ite in list(product(*[['혀', '안구', '눈', '머리', '코', '귀', '귓', '치아', '이빨', '다리',  '족지', '후지', '장',  '골격'],['없','휘','파열','파행','나오 있음', '손실', '이형', '불편', '좋 않']])) :
        disorders2.append(" ".join(ite))

    disorders = disorders1 + disorders2 + disorders3


    # ### 3)  일시적으로 보이는 증상들

    etcs1 = ['출혈', '허약', '탈수', '탈진', '마름', '무기력', '저체온', '혈변', '구토', '치석', '찰과상', '상처', '쇠약', '탈모', '기침', '비만', '몸 떨', '설사', '묽 변', '덜덜', '물 혹', '눈곱', '콧물', '침 흘', '마르', '허약','야위']

    etcs2 = []
    for ite in list(product(*[['식욕', '힘', '영양','영양 상태' '건강', '건강 상태', '기력'],['없', '부족', '불량', '안', '부진', '나쁘', '좋 않','저하']])) :
        etcs2.append(" ".join(ite))


    etcs=etcs1+etcs2

    unhealth_list = diseases+disorders+etcs

    animal_unhealth = []

    for char in animal['특징'] :

        char_unhealth = []

        for unhealth in unhealth_list :
            p = re.compile('.*'+unhealth+'.*')

            if p.search(char) :
                m=p.findall(char)
                char_unhealth.append(m)

        animal_unhealth.append(char_unhealth)

    animal['건강-'] = animal_unhealth

    # # 건강 +

    health1 = ['활발', '활기']

    health2 = []
    for ite in list(product(*[['건강','건강 상태'],['양호','좋']])) :
        health2.append(" ".join(ite))

    health3 = []
    for ite in list(product(*[['에너지', '활력'],['넘치','좋']])) :
        health2.append(" ".join(ite))

    health_list = health1 + health2 + health3

    animal_health = []

    for char in animal['특징'] :

        char_health = []

        for health in health_list :
            p = re.compile('.*'+health+'.*')

            if p.search(char) :
                m=p.findall(char)
                char_health.append(m)

        animal_health.append(char_health)

    animal['건강+'] = animal_health

    affinity_list1 = ['좋아하', '따르', '따름', '순', '친화', '호기심', '붙임성',
                      '활발', '착하', '애교', '호의', '얌전', '사교', '우호', '친밀', '명량',
                      '친근', '사랑', '활기', '쾌활', '활달',
                      '차분', '점잖', '안기', '안기려', '잘따름', '사람 자']

    affinity_list2 = []
    for ite in list(product(*[['낯가림','입질', '공격성', '피하'],['없', '않']])) :
        affinity_list2.append(" ".join(ite))

    affinity_list3 = []
    for ite in list(product(*[['사회성','성격'],['좋']])) :
        affinity_list3.append(" ".join(ite))

    affinity_list4 = []
    for ite in list(product(*[['배변'],['가리', '가림']])) :
        affinity_list4.append(" ".join(ite))

    affinity_list5 = []
    for ite in list(product(*[['훈련'],['있']])) :
        affinity_list5.append(" ".join(ite))

    affinity_list6 = []
    for ite in list(product(*[['안기', '안기려'],['좋아하']])) :
        affinity_list5.append(" ".join(ite))

    affinity_list = affinity_list1+affinity_list2+affinity_list3+affinity_list4+affinity_list5+affinity_list6


    animal_affinity = []

    for char in animal['특징'] :

        char_affinity = []

        for affinity in affinity_list :
            p = re.compile('.*'+affinity+'.*')

            if p.search(char) :
                m=p.findall(char)
                char_affinity.append(m)

        animal_affinity.append(char_affinity)

    animal['친화성+'] = animal_affinity


    # ### 2) 친화성 ↓

    unfriendly_list1 = ['위협','사나', '싸 움','사납', '경계', '겁', '소심', '쫄보', '조심', '입질', '무서워하', '낯가림', '으르렁', '예민', '까칠', '무뚝뚝', '공격성', '피하', '공격적', '돌변', '포악', '짖', '짜증', '싫어하', '거칠', '불안', '도망']


    unfriendly_list2 = []
    for ite in list(product(*[['성깔', '성격'],['있']])) :
        unfriendly_list2.append(" ".join(ite))


    unfriendly_list3 = []
    for ite in list(product(*[['따르', '숫기', '훈련', '안기', '안기려'],['않', '안', '없']])) :
        unfriendly_list3.append(" ".join(ite))


    unfriendly_list4 = []
    for ite in list(product(*[['친하 지'],['시간', '노력']])) :
        unfriendly_list4.append(" ".join(ite))


    unfriendly_list5 = []
    for ite in list(product(*[['다가가'],['힘', '없']])) :
        unfriendly_list5.append(" ".join(ite))


    unfriendly_list = unfriendly_list1+unfriendly_list2+unfriendly_list3+unfriendly_list4+unfriendly_list5


    animal_unfriendly = []

    for char in animal['특징'] :

        char_unfriendly = []

        for unfriendly in unfriendly_list :
            p = re.compile('.*'+unfriendly+'.*')

            if p.search(char) :
                m=p.findall(char)
                char_unfriendly.append(m)

        animal_unfriendly.append(char_unfriendly)

    animal['친화성-'] = animal_unfriendly


    # ## 강조

    emphasis_list = ['매우', '많', '잘', '엄청', '너무', '너무나', '굉장히', '대단히', '몹시', '무척', '심히', '아주', '심각', '심']


    # ### 친화성 + 강조

    animal_emphasis_affinity = []

    for char in animal['특징'] :

        char_emphasis_affinity = []

        for affinity in affinity_list :

            for emphasis in emphasis_list :

                p = re.compile('.*'+emphasis+'\s{0,1}'+affinity+'.*' + '|' + '.*'+affinity+'\s{0,1}'+emphasis+'.*')

                if p.search(char) :
                    m=p.findall(char)
                    char_emphasis_affinity.append(m)


        animal_emphasis_affinity.append(char_emphasis_affinity)

    animal['친화성+강조'] = animal_emphasis_affinity


    # ### 친화성 - 강조

    animal_emphasis_unfriendly = []

    for char in animal['특징'] :

        char_emphasis_unfriendly = []

        for unfriendly in unfriendly_list :

            for emphasis in emphasis_list :

                p = re.compile('.*'+emphasis+'\s{0,1}'+unfriendly+'.*' + '|' + '.*'+unfriendly+'\s{0,1}'+emphasis+'.*')

                if p.search(char) :
                    m=p.findall(char)
                    char_emphasis_unfriendly.append(m)

        animal_emphasis_unfriendly.append(char_emphasis_unfriendly)

    animal['친화성-강조'] = animal_emphasis_unfriendly


    aff_list = []
    for aff in animal['친화성+'] :
        aff_list.append(len(aff))


    unf_list = []
    for unf in animal['친화성-'] :
        unf_list.append(len(unf))


    aff_score1= [i-j for i, j in zip(aff_list, unf_list)]


    aff_list = []
    for aff in animal['친화성+강조'] :
        aff_list.append(len(aff))


    unf_list = []
    for unf in animal['친화성-강조'] :
        unf_list.append(len(unf))


    aff_score2= [i-j for i, j in zip(aff_list, unf_list)]


    aff_score= [i+j for i, j in zip(aff_score1, aff_score2)]


    animal['친화성지수'] = aff_score


    hel_list = []
    for hel in animal['건강+'] :
        hel_list.append(len(hel))


    unhel_list = []
    for unhel in animal['건강-'] :
        unhel_list.append(len(unhel))


    hel_score= [i-j for i, j in zip(hel_list, unhel_list)]


    animal['건강지수'] = hel_score


    animal['건강지수'] = hel_score
    animal['만나이'] = 2022 - animal['나이'].astype('int')
    animal['체중'] = animal['체중'].astype(float)
    animal.drop(animal.loc[animal['만나이']>9,:].index, axis=0, inplace=True)
    animal.drop(animal.loc[animal['체중']>50,:].index, axis=0, inplace=True)
    

    # ### 이상치 제거(군집화에는 있어야되고 유사도계산에는 지워야됨 357~360줄까지)

    

    return animal

    # db에서 라벨링할 데이터 추출하는 코드
    # 추출된 df를 이용해 def preprocess(animal) 호출하면 animal 리턴
    # create_model(animal)을 호출하면 유기번호, 군집라벨 출력

# data = pd.read_csv('/home/big/study/roadpet_etl/datajob/etl/data/raw_data.csv')
# preprocess(data)