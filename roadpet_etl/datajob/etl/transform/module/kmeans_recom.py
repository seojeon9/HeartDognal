import joblib

def recommend(animal) :
    feature = animal[['만나이', '체중_숫자', 'api_친화성', 'api_건강점수']]
    minmax = joblib.load('datajob/etl/transform/model/minmax(20000).pkl')
    feature_minmax = minmax.transform(feature)
    model = joblib.load("datajob/etl/transform/model/kmeans(20000,60).pkl")
    cluster_list = model.predict(feature_minmax)
    animal['군집'] = cluster_list
    return animal
