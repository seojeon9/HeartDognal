import joblib

def recommend(animal) :
    feature = animal[['만나이', '체중', '친화성지수', '건강지수']]
    stdsc = joblib.load('datajob/etl/transform/model/stdscaler(20000,konlpy).pkl')
    feature_stdsc = stdsc.transform(feature)
    model = joblib.load("datajob/etl/transform/model/kmeans(20000,konlpy).pkl")
    cluster_list = model.predict(feature_stdsc)
    animal['군집'] = cluster_list
    return animal
