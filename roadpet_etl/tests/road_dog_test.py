import unittest
from datajob.etl.extract.road_dog_extract import RoadDogExtractor
from datajob.etl.transform.module.content_sim import ContentSimPreprocess
from datajob.etl.transform.road_dog_transform import RoadDogTrasformer

class MTest(unittest.TestCase):
    def test1(self):
        RoadDogExtractor.extract_data()

    def test2(self):
        RoadDogTrasformer.transform()
    
    def test3(self):
        ContentSimPreprocess.content_sim_preprocess()




if __name__ == "__main__":
    """ This is executed when run from the command line """
    unittest.main()