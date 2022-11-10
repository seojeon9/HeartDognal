import pandas as pd
import re
import numpy as np
from sklearn.metrics import silhouette_samples, silhouette_score
from sklearn.cluster import KMeans
import joblib 
from sklearn.preprocessing import MinMaxScaler
from scipy.spatial.distance import cosine
from sklearn.metrics.pairwise import cosine_similarity
import kmeans_recom


def create_model(animal) :

    # 군집 라벨 부착
    animal = kmeans_recom.recommend(animal)
    return animal[['유기번호','군집']]
