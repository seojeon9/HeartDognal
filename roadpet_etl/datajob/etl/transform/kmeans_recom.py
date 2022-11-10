from sklearn.cluster import KMeans
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import joblib

def recommend(animal) :
    feature = animal[['나이_주환산', '체중', 'api_친화성', 'api_건강점수']]
    minmax = joblib.load('minmaxscaler.pkl')
    feature_minmax = minmax.transform(feature)
    model = joblib.load("kmeans.pkl")
    cluster_list = model.predict(feature_minmax)
    animal['군집'] = cluster_list
    return animal
