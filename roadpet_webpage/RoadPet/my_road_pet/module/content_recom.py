import joblib

# 유기번호가 입력되면 그 유기번호를 가진 동물과 유사한 동물 10개의 유기번호가 리스트로 출력
def recommend(dog_regno) :
    dogs_sim10_regno = joblib.load("./my_road_pet/data/dogs_sim10_regno.pkl")
    sim10_reg_list = dogs_sim10_regno[dog_regno]
    return sim10_reg_list
