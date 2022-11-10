from sklearn.cluster import KMeans
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import joblib


def recommend(dog_regno) :
    dogs_sim10_regno = joblib.load("./my_road_pet/data/preprocessed_data/dogs_sim10_regno.csv")
    dog = pd.read_csv("./my_road_pet/data/preprocessed_data/preprocessed_dog.csv", index_col=0)
    sim10_reg_list = dogs_sim10_regno[dog_regno]
    dog_sim10 = dog.loc[dog.유기번호.isin(sim10_reg_list), :]
    return dog_sim10