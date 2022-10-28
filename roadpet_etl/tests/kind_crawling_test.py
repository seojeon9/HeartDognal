import unittest
from datajob.etl.extract.kind_api_extract import KindExtract
from datajob.etl.extract.kind_crawling_extract import DogKindExtractor



class MTest(unittest.TestCase):
    def test1(self):
        DogKindExtractor.extract_data()

    def test2(self):
        KindExtract.extract_data()

if __name__ == "__main__":
    """ This is executed when run from the command line """
    unittest.main()