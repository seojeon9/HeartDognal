import unittest
from datajob.etl.extract.shelter_detail_extract import ShelterDetailExtract
from datajob.etl.extract.shelter_extract import ShelterExtract
from datajob.etl.extract.sido_extract import SidoExtract
from datajob.etl.extract.sigungu_extract import SigunguExtract
from datajob.etl.transform.shelter_transform import ShelterTrasformer
from datajob.etl.transform.sigungu_transform import SigunguTrasformer
from datajob.etl.transform.sido_transform import SidoTrasformer


class MTest(unittest.TestCase):
    def test1(self):
        SidoExtract.extract_data()

    def test2(self):
        SigunguExtract.extract_data()

    def test3(self):
        ShelterExtract.extract_data()

    def test4(self):
        ShelterDetailExtract.extract_data()

    def test5(self):
        SidoTrasformer.transform()

    def test6(self):
        SigunguTrasformer.transform()

    def test7(self):
        ShelterTrasformer.transform()


if __name__ == "__main__":
    """ This is executed when run from the command line """
    unittest.main()
