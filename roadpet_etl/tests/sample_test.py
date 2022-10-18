import unittest
from datajob.etl.extract.daily_box_office_api import DailyBoxOfficeExtractor
from datajob.etl.transform.daily_box_offce_transform import DailyBoxOfficeTransformer


class MTest(unittest.TestCase):
    # def test1(self):
    #     DailyBoxOfficeExtractor.extract_data(3)

    def test1(self):
        DailyBoxOfficeTransformer.transform()


if __name__ == "__main__":
    """ This is executed when run from the command line """
    unittest.main()
