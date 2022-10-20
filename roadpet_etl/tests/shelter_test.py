import unittest
from datajob.etl.extract.shelter_extract import ShelterExtract
from datajob.etl.extract.sido_extract import SidoExtract
from datajob.etl.extract.sigungu_extract import SigunguExtract


class MTest(unittest.TestCase):
    def test1(self):
        SidoExtract.extract_data()

    def test2(self):
        SigunguExtract.extract_data()

    def test3(self):
        ShelterExtract.extract_data()


if __name__ == "__main__":
    """ This is executed when run from the command line """
    unittest.main()
