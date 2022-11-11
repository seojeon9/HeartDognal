from datajob.etl.transform.module.kmeans_recom import recommend


def create_model(animal) :

    # 군집 라벨 부착
    animal = recommend(animal)
    return animal[['유기번호','군집']]
