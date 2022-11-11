from sklearn.cluster import KMeans
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import joblib

def recommend(sample) :
    minmax = joblib.load('./my_road_pet/model/minmax(20000).pkl')
    sample_minmax = minmax.transform(sample)
    model = joblib.load("./my_road_pet/model/kmeans(20000,60).pkl")
    sample_cluster = model.predict(sample_minmax)[0]
    return sample_cluster
