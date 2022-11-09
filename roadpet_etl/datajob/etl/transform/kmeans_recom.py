from sklearn.cluster import KMeans
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import joblib

def recommend(sample) :
    minmax = joblib.load('./my_road_pet/model/minmaxscaler.pkl')
    sample_minmax = minmax.transform(sample)
    model = joblib.load("./my_road_pet/model/kmeans.pkl")
    sample_cluster = model.predict(sample_minmax)[0]
    dog = pd.read_csv('./my_road_pet/data/preprocessed_data/preprocessed_dog.csv', index_col=0)
    dog_recom = dog.loc[dog['군집']==sample_cluster, :]
    return dog_recom
