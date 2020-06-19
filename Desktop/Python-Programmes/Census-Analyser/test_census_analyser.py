from census_analyser import CensusAnalyser
from census_analyser_exception import CensusAnalyserError

class TestCensusAnalyser:
    CENSUS_CSV_FILE_PATH = "IndiaStateCensusData.csv"
    CENSUS_WRONG_CSV_FILE_PATH = "/home/IndiaStateCensusData.csv"
    CENSUS_WRONG_DELIMITER_FILE = "CensusInvalidDelimiter.csv"

    def test_given_indian_census_CSV_file_returns_correct_records(self):
        census_analyser = CensusAnalyser()
        num_of_records = census_analyser.load_india_census_data(
                        TestCensusAnalyser.CENSUS_CSV_FILE_PATH)
        assert num_of_records == 29

    def test_given_india_census_data_with_wrong_file_should_throw_exception(self):
        try:
            census_analyser = CensusAnalyser()
            num_of_records = census_analyser.load_india_census_data(
                            TestCensusAnalyser.CENSUS_CSV_FILE_PATH)
        except CensusAnalyserError as exception:
            assert exception.exception_type == CensusAnalyserError.ExceptionType.FILE_NOT_FOUND

    def test_given_india_census_file_with_wrong_delimiter_should_throw_exception(self):
        try:
            census_analyser = CensusAnalyser()
            num_of_records = census_analyser.load_india_census_data(
                            TestCensusAnalyser.CENSUS_WRONG_DELIMITER_FILE)
        except CensusAnalyserError as exception:
            assert exception.exception_type == CensusAnalyserError.ExceptionType.FILE_NOT_FOUND
