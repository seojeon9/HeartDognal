import unittest
from datajob.etl.extract.kind_api_extract import KindExtract
from datajob.etl.extract.kind_crawling_extract import DogKindExtractor
from datajob.etl.transform.classified_dog_transform import ClassifiedDog
from datajob.etl.transform.kind_feature_transform import KindFeature



class MTest(unittest.TestCase):
    def test1(self):
        DogKindExtractor.extract_data()

    def test2(self):
        KindExtract.extract_data()

    def test3(self):
        KindFeature.transform()

    def test4(self):
        ClassifiedDog.transform()
    

if __name__ == "__main__":
    """ This is executed when run from the command line """
    unittest.main()