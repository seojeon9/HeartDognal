import unittest
from datajob.etl.extract.kind_api_extract import KindExtract
from datajob.etl.transform.shelter_op_transform import ShelterOpTrasformer
from datajob.etl.transform.sido_op_transform import SidoOpTrasformer
from datajob.etl.transform.sigungu_op_transform import SigunguOpTrasformer


class MTest(unittest.TestCase):
    def test1(self):
        SidoOpTrasformer.transform()

    def test2(self):
        SigunguOpTrasformer.transform()

    def test3(self):
        ShelterOpTrasformer.transform()

    def test4(self):
        KindExtract.extract()


if __name__ == "__main__":
    """ This is executed when run from the command line """
    unittest.main()
