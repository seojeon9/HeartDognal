#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import re
import numpy as np
from sklearn.metrics import silhouette_samples, silhouette_score
from sklearn.cluster import KMeans
import joblib 
from sklearn.preprocessing import MinMaxScaler
from scipy.spatial.distance import cosine
from sklearn.metrics.pairwise import cosine_similarity


# In[3]:


animal = pd.read_csv('../data/raw_data/animal(221029).csv', index_col = 0)


# ### 보호중인 동물만

# In[4]:


animal=animal.loc[animal['상태']=='보호중',:]


# ### 강아지만 추출

# In[5]:


p = re.compile('[개]')

animal['품종'] = animal['품종'].astype('str')

dog_index = []

for i, a in enumerate(animal['품종']) :
    if p.search(a) :
        dog_index.append(i)
        
animal = animal.iloc[dog_index, :]

animal.reset_index(inplace=True)


# ### 나이 이상한 값 제거

# In[6]:


p = re.compile('(\d){4}\(년생\)')

drop_list = []
for index, a in enumerate(animal['나이']) :
    
    if p.search(a) == None :
        drop_list.append(index)
                
animal = animal.drop(drop_list, axis = 0)
animal.reset_index(inplace=True)


# In[7]:


animal.loc[animal['index']==4361, :]


# ## 건강

# ### 1) 질병

# In[8]:


# diseases = ['감염','염증', '피부염', '결막염', '피부명', '질병', '질환', '증상', '실조', '발작', '곤란', '사상충', '종양', '배농피증', '증세', '양성', '잠복', '장파열', '허니아', '백내장', '디스템퍼', '개선충', '진드기', '안충', '폐렴', '코로나', '손상']


# In[9]:


# animal_disease = []

# for char in animal['특징'] :
    
#     char_disease = []
    
#     for disease in diseases :        
#         p = re.compile(('.*'+disease+'.*'))
        
#         if p.search(char) :
#             m=p.findall(char)
#             char_disease.append(m)
        
#     animal_disease.append(char_disease)

# animal['질병'] = animal_disease


# ### 2) 장애

# In[10]:


# disorders = ['족지', '좌측후지', '골절', '절단', '기립', '못함', '마비', '교통사고', '사고', '상해', '불가', '불가능', '불능', '절음', '탈구', '탈골', '외상', '부정교합', '치아없음', '기형', '의식없음', '보행이상', '사고의심']


# In[11]:


# animal_disorder = []

# for char in animal['특징'] :
    
#     char_disorder = []
    
#     for disorder in disorders :
        
#         p = re.compile('.*'+disorder+'.*')
        
#         if p.search(char) :
#             m=p.findall(char)
#             char_disorder.append(m)
        
        
#     animal_disorder.append(char_disorder)

# animal['장애'] = animal_disorder


# ### 3)  일시적으로 보이는 증상들

# In[12]:


# etcs = ['영양상태', '출혈', '기력', '허약', '식욕부진', '임신', '탈수', '탈진', '무기력', '힘이없음', '설사', '눈곱', '콧물', '침흘림', '저체온', '진드기', '혈변', '거품토', '탯줄', '치석', '찰과상', '상처', '쇠약', '탈모', '기침', '비만']


# In[13]:


# animal_etc = []

# for char in animal['특징'] :
    
#     char_etc = []
    
#     for etc in etcs :        
#         p = re.compile('.*'+etc+'.*')
        
#         if p.search(char) :
#             m=p.findall(char)
#             char_etc.append(m)
        
#     animal_etc.append(char_etc)
    
# animal['일시증상'] = animal_etc


# # 건강

# In[14]:


pain_list = ['감염','염증', '병변', '피부', '이염', '결막염', '질병', '질환', '증상', '실조', '발작', '곤란', '사상충', '종양', '배농피증', '증세', '양성', '잠복', '장파열', '허니아', '백내장', '디스템퍼', '개선충', '진드기', '안충', '폐렴', '코로나', '손상', '백내장',
       '족지', '좌측후지', '장애', '골절', '절단', '기립', '못함', '마비', '교통사고', '사고', '상해', '불가', '불가능', '불능', '절음', '절고', '절뚝', '탈구', '탈골', '외상', '부정교합', '치아없음', '기형', '의식없음', '보행이상', '사고의심', '안구', '휘어',  '파행', '파열', '나와있음', '실명',
       '영양상태', '출혈', '기력', '허약', '식욕부진', '식욕없음', '식욕 없음', '임신', '탈수', '탈진', '탈장', '마름', '무기력', '힘이없음', '설사', '눈곱', '콧물', '침흘림', '저체온', '진드기', '혈변', '거품토', '탯줄', '치석', '찰과상', '상처', '쇠약', '탈모', '기침', '비만', '몸떪', '묽은변', '덜덜', '물혹']


# In[15]:


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

# In[16]:


affinity_list = ['좋아', '따름', '따른', '따르', '온순', '순함', '순한', '순하', '순둥', '순딩', '순종', '친화', '호기심', 
                  '활발', '착함', '착한', '밝은', '밝고', '애교', '호의', '얌전', '사교', '우호', '친밀', '명량', 
                  '친근', '사랑스', '활기', '쾌활', '활달', '낯가림 없음', '입질없음', '사회성', '성격좋은', 
                  '성격 좋은', '차분', '점잖', '안기는', '배변가림', '배변 가림', '배변가리고', '배변 가리고', '낯가림없음', '낯가림 없음', '공격성 없음', '공격성없음']


# In[17]:


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

# In[18]:


unfriendly_list = ['위협','사나움', '사나운', '싸나움', '사납', '경계', '겁', '소심', '쫄보', '입질', '무서워', '무서운', '낯가림', '낯가리', '으르렁', '예민', '까칠', '무뚝뚝', '공격성', '따르지 않음', '친화 노력', '사람손피함', '공격적', '숫기가 없', '돌변', '포악', '짖음', '짖는', '짖다' '훈련안됨', '짜증', '성격있음', '성격 있음', '싫어', '안기려하지는 않음', '거칠', '피함', '불안', '다가가기']


# In[19]:


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

# In[20]:


emphasis_list = ['매우', '많이', '많은', '많고', '잘', '엄청', '너무', '너무나', '굉장히', '대단히', '몹시', '무척', '심히', '아주', '심각', '심함', '나쁨', '불량']


# In[21]:


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

# In[22]:


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


# In[23]:


aff_list = []
for aff in animal['친화성+'] :
    aff_list.append(len(aff))


# In[24]:


unf_list = []
for unf in animal['친화성-'] :
    unf_list.append(len(unf))


# In[25]:


aff_score1= [i-j for i, j in zip(aff_list, unf_list)]


# In[26]:


aff_list = []
for aff in animal['친화성+강조'] :
    aff_list.append(len(aff))


# In[27]:


unf_list = []
for unf in animal['친화성-강조'] :
    unf_list.append(len(unf))


# In[28]:


aff_score2= [i-j for i, j in zip(aff_list, unf_list)]


# In[29]:


aff_score= [i+j for i, j in zip(aff_score1, aff_score2)]


# In[30]:


animal['api_친화성'] = aff_score


# In[31]:


pain_score = []
for pain in animal['건강'] :
    pain_score.append(7-len(pain))


# In[32]:


animal['api_건강점수'] = pain_score


# #### 친화성 score

# In[33]:


# animal['친화성_score'] = animal['api_친화성']

# animal.loc[animal['친화성'] == '높음', '친화성_score'] = animal.loc[animal['친화성'] == '높음', '친화성_score'] + 2
# animal.loc[animal['친화성'] == '낮음', '친화성_score'] = animal.loc[animal['친화성'] == '높음', '친화성_score'] - 2
# animal.loc[animal['친화성_score'].isnull()==True, '친화성_score'] = 0


# ### 연령

# In[34]:


age_list = ['개월', '주', '일']


# In[35]:


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

# In[36]:


year_list = []
for a in animal['나이'] :
    year = a.strip('(년생)')
    year_list.append(year)


# In[37]:


animal['출생연도'] = year_list


# In[38]:


animal['출생연도'].unique()


# In[39]:


animal['만나이'] = 2022 - animal['출생연도'].astype('int')


# In[40]:


month = re.compile('(\d+[.]){0,1}\d+개월')
week = re.compile('(\d+[.]){0,1}\d+주')
day = re.compile('(\d+[.]){0,1}\d+일')
num = re.compile('(\d+[.]){0,1}\d+')


# In[41]:


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


# In[42]:


animal['1년미만_주환산'] = age_list


# In[43]:


animal['1년이상_주환산'] = animal['만나이'] * 52


# In[44]:


week_age_list = []
for a, b in zip(animal['1년미만_주환산'], animal['1년이상_주환산']) :
    if a == 'None' and b == 0 :
        week_age_list.append(27)
    elif a == 'None' and b != 0 :
        week_age_list.append(b)
    else :
        week_age_list.append(a)


# In[45]:


animal['나이_주환산'] = week_age_list


# ## 체중

# In[49]:


p = re.compile('(\d+[.]){0,1}\d+\(Kg\)')


# In[50]:


a_index = []
b = []

for i, a in enumerate(animal['체중']) :
    if p.search(a) == None :
        a_index.append(i)
        b.append(animal['체중'][i])


# In[51]:


p = re.compile('(\d+[.]){0,1}\d+')


# In[52]:


weight_list = []
for a in animal['체중'] :
    weight_list.append(p.search(a).group())


# In[53]:


animal['체중_숫자'] = weight_list


# In[54]:


animal['체중_숫자'] = animal['체중_숫자'].astype(float)


# ### 성별

# In[56]:


animal = pd.concat([animal, pd.get_dummies(animal['성별'])], axis=1)


# ### 중성화

# In[57]:


animal = pd.concat([animal, pd.get_dummies(animal['중성화여부'])], axis=1)



# ## 모델링

# ### 1) 군집화 모델 저장

# In[74]:


feature = animal[['나이_주환산', '체중_숫자', 'api_친화성', 'api_건강점수']]
minmaxscaler = MinMaxScaler()
minmaxscaler.fit(feature)
joblib.dump(minmaxscaler, '../model/minmaxscaler.pkl')
animal_minmax_scaled = minmaxscaler.transform(feature)

kmeans = KMeans(n_clusters=50, init='k-means++', max_iter=1000, random_state=1).fit(animal_minmax_scaled)

animal['군집'] = kmeans.labels_

animal.to_csv('../data/preprocessed_data/preprocessed_dog.csv', index=False)
# In[75]:


joblib.dump(kmeans, '../model/kmeans.pkl')


# ### 2) 콘텐츠 유사도 저장

# In[88]:


animal_cos_sim = cosine_similarity(animal_minmax_scaled, animal_minmax_scaled)


# In[77]:


# animal_cos_sim


# In[78]:


# animal_sim=animal_cos_sim.argsort(axis=1)


# In[79]:


# animal_sim


# In[87]:


# np.flip(animal_sim, axis=1)


# In[91]:


sim10_index=np.flip(animal_cos_sim.argsort(axis=1), axis=1)[:,1:11]

dogs_sim_reg = []
for i in range(sim10_index.shape[0]) :
    dog_sim_reg = []
    for j in range(sim10_index.shape[1]) :
        dog_sim_reg.append(animal.iloc[sim10_index[i][j]]['유기번호'])
    dogs_sim_reg.append(dog_sim_reg)

dogs_sim_reg = np.array(dogs_sim_reg)


sim_dict = {}

for i in range(len(dogs_sim_reg)) :
    sim_dict[animal.iloc[i]['유기번호']] = dogs_sim_reg[i]

# In[94]:

joblib.dump(sim_dict, '../data/preprocessed_data/dogs_sim10_regno.csv')


# In[ ]:




