import unittest
from census_analyser import CensusAnalyser

class TestCensusAnalyser(unittest.TestCase):
    INDIA_CENSUS_CSV_FILE_PATH = """IndiaStateCensusData.csv"""

    def test_load_india_census_data(self):
        census_analyser = CensusAnalyser()
        num_of_records = census_analyser.load_india_census_data(
                            TestCensusAnalyser.INDIA_CENSUS_CSV_FILE_PATH)
        self.assertEqual(num_of_records, 29)
            
if __name__ == "__main__":
    unittest.main()
    