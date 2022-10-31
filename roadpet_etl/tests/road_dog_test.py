import unittest
from datajob.etl.extract.kind_crawling_extract import DogKindExtractor
from datajob.etl.extract.road_dog_extract import RoadDogExtractor
from datajob.etl.transform.color_df_generate import ColorDictGenerator
from datajob.etl.transform.color_transform import ColorTransformer
from datajob.etl.transform.road_dog_transform import RoadDogTrasformer

class MTest(unittest.TestCase):
    def test1(self):
        RoadDogExtractor.extract_data()

    def test2(self):
        RoadDogTrasformer.transform()

    def test3(self):
        DogKindExtractor.extract_data()
    
    def test4(self):
        ColorDictGenerator.generate()
    
    def test5(self):
        ColorTransformer.transform()



if __name__ == "__main__":
    """ This is executed when run from the command line """
    unittest.main()