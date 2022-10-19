import unittest
from datajob.etl.extract.sido_extract import SidoExtract


class MTest(unittest.TestCase):
    def test1(self):
        SidoExtract.extract_data()


if __name__ == "__main__":
    """ This is executed when run from the command line """
    unittest.main()
