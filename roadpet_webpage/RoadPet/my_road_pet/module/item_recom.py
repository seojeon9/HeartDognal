# 데이터프레임에 피봇테이블을 적용하는 함수 : to_piv_table(score_df)
# 피봇테이블로 아이템간 유사도를 구하고 데이터프레임으로 반환하는 함수 : get_sim(scores_matrix)

# import pandas as pd
# import numpy as np
# from sklearn.metrics.pairwise import cosine_similarity

def to_piv_table(score_df) :
    scores_matrix = score_df.pivot_table('score', index='userId', columns='dogId')
    scores_matrix = scores_matrix.fillna(0)

    return scores_matrix

def get_sim(scores_matrix) :
    scores_matrix_T = scores_matrix.T
    item_sim = cosine_similarity(scores_matrix_T, scores_matrix_T)
    item_sim_df = pd.DataFrame(item_sim, index=scores_matrix.columns, columns=scores_matrix.columns)

    return item_sim_df

# ----------------------------------------------------------------------------------------------------

# 사용자별 아이템 유사도에 기반한 예측 평점 데이터 세트 반환하는 함수(df로)
# ratings_arr : 평점 매트릭스를 array화 시킨 것 [ex) scores_matrix.values]
# item_sim_arr : 아이템 유사도 df를 array화 [ex) item_sim_df.values]

def predict_rating_topsim(ratings_arr, item_sim_arr, n=20):
    # 사용자-아이템 평점 행렬 크기만큼 0으로 채운 예측 행렬 초기화
    pred = np.zeros(ratings_arr.shape)
    # 모든 사용자에 대해서 모든 유기견의 평점예측을 진행할 초기 행렬

    # 사용자-아이템 평점 행렬의 열 크기만큼 Loop 수행.
    for col in range(ratings_arr.shape[1]):
        # 유사도 행렬에서 유사도가 큰 순으로 n개 데이터 행렬의 index 반환
        top_n_items = [np.argsort(item_sim_arr[:, col])[:-n - 1:-1]]
        # 개인화된 예측 평점을 계산(위 수식을 대입)
        for row in range(ratings_arr.shape[0]):
            pred[row, col] = item_sim_arr[col, :][top_n_items].dot(ratings_arr[row, :][top_n_items].T)
            pred[row, col] /= np.sum(np.abs(item_sim_arr[col, :][top_n_items]))

    scores_pred_matrix = pd.DataFrame(data=scores_pred, index=scores_matrix.index,
                                      columns=scores_matrix.columns)
    return scores_pred_matrix

# ----------------------------------------------------------------------------------------------------

# 선호도를 주지 않은 유기견을 리스트 객체로 반환하는 함수 : get_unseen_dogs(ratings_matrix, userId)
# 유기견 추천 함수 : recomm_dog_by_userid(pred_df, userId, unseen_list, top_n=10)

def get_unseen_dogs(ratings_matrix, userId):
    # userId로 입력받은 사용자의 모든 유기견 평점 정보 추출하여 Series로 반환
    user_rating = ratings_matrix.loc[userId, :]
    # 반환된 user_rating 은 유기견(dogId)를 index로 가지는 Series 객체임
    unseen_list = user_rating[user_rating == 0].index.to_list()

    return unseen_list

def recomm_dog_by_userid(pred_df, userId, unseen_list, top_n=10):
    # 예측 평점 DataFrame(pred_df)에서 사용자id index와 unseen_list로 들어온 dogId 컬럼을 추출하여
    # 가장 예측 평점이 높은 순으로 정렬함.(top_n개 만큼)
    # pred_df.loc[userId, unseen_list] : 평점을 부여하지 않은 유기견들에 대한 예측평점 data 추출
    recomm_dogs = pred_df.loc[userId, unseen_list].sort_values(ascending=False)[:top_n]
    return recomm_dogs

