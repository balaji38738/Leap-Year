from census_analyser import Analyser
from census_analyser_exception import AnalyserError
from csv_state_census import CSVStateCensus
from csv_states import CSVStates

class TestCensusAnalyser:
    CENSUS_CSV_FILE_PATH = "IndiaStateCensusData.csv"
    CENSUS_WRONG_CSV_FILE_PATH = "/home/IndiaStateCensusData.csv"
    CENSUS_WRONG_DELIMITER_FILE = "CensusInvalidDelimiter.csv"
    CENSUS_WRONG_EXTENSION_FILE = "IndiaStateCensusData.txt"
    CENSUS_WRONG_HEADER_FILE = "CensusWrongHeader.csv"

    STATE_CODE_CSV_FILE_PATH = "IndiaStateCode.csv"
    STATE_CODE_WRONG_CSV_FILE_PATH = "/home/IndiaStateCode.csv"
    STATE_CODE_WRONG_DELIMITER_FILE = "StateCodeWrongDelimiter.csv"
    STATE_CODE_WRONG_EXTENSION_FILE = "IndiaStateCode.txt"
    STATE_CODE_WRONG_HEADER_FILE = "StateCodeWrongHeader.csv"

    def test_given_indian_census_CSV_file_returns_correct_records(self):
        analyser = Analyser()
        census_num_of_records = analyser.analyse_csv_data(
                        TestCensusAnalyser.CENSUS_CSV_FILE_PATH, CSVStateCensus)
        state_code_num_of_records = analyser.analyse_csv_data(
                        TestCensusAnalyser.STATE_CODE_CSV_FILE_PATH, CSVStates)
        assert census_num_of_records == 29
        assert state_code_num_of_records == 37

    def test_given_file_with_wrong_path_should_throw_exception(self):
        try:
            analyser = Analyser()
            census_num_of_records  = analyser.analyse_csv_data(
                            TestCensusAnalyser.CENSUS_WRONG_CSV_FILE_PATH, CSVStateCensus)
            state_code_num_of_records = analyser.analyse_csv_data(
                            TestCensusAnalyser.STATE_CODE_WRONG_CSV_FILE_PATH, CSVStates)
        except AnalyserError as exception:
            assert exception.exception_type == AnalyserError.ExceptionType.FILE_NOT_FOUND

    def test_given_file_with_wrong_delimiter_should_throw_exception(self):
        try:
            analyser = Analyser()
            census_num_of_records  = analyser.analyse_csv_data(
                            TestCensusAnalyser.CENSUS_WRONG_DELIMITER_FILE, CSVStateCensus)
            state_code_num_of_records = analyser.analyse_csv_data(
                            TestCensusAnalyser.STATE_CODE_WRONG_DELIMITER_FILE, CSVStates)
        except AnalyserError as exception:
            assert exception.exception_type == AnalyserError.ExceptionType.WRONG_DELIMITER

    def test_given_file_with_wrong_extension_should_throw_exception(self):
        try:
            analyser = Analyser()
            census_num_of_records  = analyser.analyse_csv_data(
                            TestCensusAnalyser.CENSUS_WRONG_EXTENSION_FILE, CSVStateCensus)
            state_code_num_of_records = analyser.analyse_csv_data(
                            TestCensusAnalyser.STATE_CODE_WRONG_EXTENSION_FILE, CSVStates)
        except AnalyserError as exception:
            assert exception.exception_type == AnalyserError.ExceptionType.WRONG_EXTENSION

    def test_given_file_with_wrong_header_should_throw_exception(self):
        try:
            analyser = Analyser()
            census_num_of_records  = analyser.analyse_csv_data(
                            TestCensusAnalyser.CENSUS_WRONG_HEADER_FILE, CSVStateCensus)
            state_code_num_of_records = analyser.analyse_csv_data(
                            TestCensusAnalyser.STATE_CODE_WRONG_HEADER_FILE, CSVStates)
        except AnalyserError as exception:
            assert exception.exception_type == AnalyserError.ExceptionType.WRONG_HEADER

