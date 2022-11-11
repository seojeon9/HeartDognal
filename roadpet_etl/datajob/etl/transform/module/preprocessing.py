import pandas as pd
import re



def preprocess(animal) :

    # 나이 형식에 안맞는 값 제거
    animal['나이'] = animal['나이'].astype('str')
    p = re.compile('(\d){4}')

    drop_list = []
    for index, a in enumerate(animal['나이']):

        if p.search(a) == None:
            drop_list.append(index)

    animal = animal.drop(drop_list, axis=0)
    animal.reset_index(inplace=True)

    # 체중 형식에 안맞는 값 제거
    p = re.compile('(\d+[.]){0,1}\d+')

    drop_list = []
    for index, a in enumerate(animal['체중']):

        if p.search(a) == None:
            drop_list.append(index)

    animal = animal.drop(drop_list, axis=0)
    animal.reset_index(inplace=True)


    pain_list = ['감염','염증', '병변', '피부', '이염', '결막염', '질병', '질환', '증상', '실조', '발작', '곤란', '사상충', '종양', '배농피증', '증세', '양성', '잠복', '장파열', '허니아', '백내장', '디스템퍼', '개선충', '진드기', '안충', '폐렴', '코로나', '손상', '백내장',
           '족지', '좌측후지', '장애', '골절', '절단', '기립', '못함', '마비', '교통사고', '사고', '상해', '불가', '불가능', '불능', '절음', '절고', '절뚝', '탈구', '탈골', '외상', '부정교합', '치아없음', '기형', '의식없음', '보행이상', '사고의심', '안구', '휘어',  '파행', '파열', '나와있음', '실명',
           '영양상태', '출혈', '기력', '허약', '식욕부진', '식욕없음', '식욕 없음', '임신', '탈수', '탈진', '탈장', '마름', '무기력', '힘이없음', '설사', '눈곱', '콧물', '침흘림', '저체온', '진드기', '혈변', '거품토', '탯줄', '치석', '찰과상', '상처', '쇠약', '탈모', '기침', '비만', '몸떪', '묽은변', '덜덜', '물혹']



    animal_pain = []

    for char in animal['특징'] :

        char_pain = []

        for pain in pain_list :
            p = re.compile('.*'+pain+'.*')

            if p.search(char) :
                m=p.findall(char)
                char_pain.append(m)

        animal_pain.append(char_pain)

    animal['건강'] = animal_pain


    # ## 성격

    # ### 1) 친화성 ↑


    affinity_list = ['좋아', '따름', '따른', '따르', '온순', '순함', '순한', '순하', '순둥', '순딩', '순종', '친화', '호기심',
                      '활발', '착함', '착한', '밝은', '밝고', '애교', '호의', '얌전', '사교', '우호', '친밀', '명량',
                      '친근', '사랑스', '활기', '쾌활', '활달', '낯가림 없음', '입질없음', '사회성', '성격좋은',
                      '성격 좋은', '차분', '점잖', '안기는', '배변가림', '배변 가림', '배변가리고', '배변 가리고', '낯가림없음', '낯가림 없음', '공격성 없음', '공격성없음']


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


    unfriendly_list = ['위협','사나움', '사나운', '싸나움', '사납', '경계', '겁', '소심', '쫄보', '입질', '무서워', '무서운', '낯가림', '낯가리', '으르렁', '예민', '까칠', '무뚝뚝', '공격성', '따르지 않음', '친화 노력', '사람손피함', '공격적', '숫기가 없', '돌변', '포악', '짖음', '짖는', '짖다' '훈련안됨', '짜증', '성격있음', '성격 있음', '싫어', '안기려하지는 않음', '거칠', '피함', '불안', '다가가기']


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

    # ### 친화성 + 강조

    emphasis_list = ['매우', '많이', '많은', '많고', '잘', '엄청', '너무', '너무나', '굉장히', '대단히', '몹시', '무척', '심히', '아주', '심각', '심함', '나쁨', '불량']



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


# 점수계산


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

    animal['api_친화성'] = aff_score

    pain_score = []
    for pain in animal['건강'] :
        pain_score.append(7-len(pain))

    animal['api_건강점수'] = pain_score


    # #### 친화성 score


    age_list = ['개월', '주', '일']



    animal_age = []

    for char in animal['특징'] :

        char_age = []

        for age in age_list :
            p = re.compile('(\d+[.])*\d+'+age)

            if p.search(char) :
                m=p.search(char)
                char_age.append(m.group())

        animal_age.append(char_age)

    animal['1년미만'] = animal_age


    # ## 나이


    animal['만나이'] = 2022 - animal['나이'].astype('int')


    month = re.compile('(\d+[.]){0,1}\d+개월')
    week = re.compile('(\d+[.]){0,1}\d+주')
    day = re.compile('(\d+[.]){0,1}\d+일')
    num = re.compile('(\d+[.]){0,1}\d+')

    age_list = []

    animal['1년미만'] = animal['1년미만'].astype('str')

    for a in animal['1년미만'] :
        if month.search(a) :
            week_num = float(num.search(a).group()) * 4.5
            age_list.append(week_num)
            pass

        elif week.search(a) :
            week_num = float(num.search(a).group())
            age_list.append(week_num)
            pass

        elif day.search(a) :
            week_num = float(num.search(a).group()) / 7
            age_list.append(week_num)
            pass

        else :
            age_list.append('None')

    animal['1년미만_주환산'] = age_list

    animal['1년이상_주환산'] = animal['만나이'] * 52

    week_age_list = []
    for a, b in zip(animal['1년미만_주환산'], animal['1년이상_주환산']) :
        if a == 'None' and b == 0 :
            week_age_list.append(27)
        elif a == 'None' and b != 0 :
            week_age_list.append(b)
        else :
            week_age_list.append(a)

    animal['나이_주환산'] = week_age_list

    # 체중
    p = re.compile('(\d+[.]){0,1}\d+')
    weight_list = []
    for a in animal['체중']:
        weight_list.append(p.search(a).group())
    animal['체중_숫자'] = weight_list
    animal['체중_숫자'] = animal['체중_숫자'].astype(float)
    animal.drop(animal.loc[animal['만나이'] > 9, :].index, axis=0, inplace=True)
    animal.drop(animal.loc[animal['체중_숫자'] > 50, :].index, axis=0, inplace=True)
    
    return animal

    # db에서 라벨링할 데이터 추출하는 코드
    # 추출된 df를 이용해 def preprocess(animal) 호출하면 animal 리턴
    # create_model(animal)을 호출하면 유기번호, 군집라벨 출력