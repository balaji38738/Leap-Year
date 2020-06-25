from census_analyser import Analyser
from census_analyser_exception import AnalyserError
from csv_state_census import CSVStateCensus
from csv_states import CSVStates
import json
from us_census_csv import USCensusCSV

class TestCensusAnalyser:
    INDIA_CENSUS_CSV_FILE_PATH = ".//Resources//IndiaStateCensusData.csv"
    INDIA_CENSUS_WRONG_CSV_FILE_PATH = "//home//IndiaStateCensusData.csv"
    CENSUS_WRONG_DELIMITER_FILE = ".//Resources//CensusInvalidDelimiter.csv"
    INDIA_CENSUS_WRONG_EXTENSION_FILE = ".//Resources//IndiaStateCensusData.txt"
    INDIA_CENSUS_WRONG_HEADER_FILE = ".//Resources//CensusWrongHeader.csv"

    STATE_CODE_CSV_FILE_PATH = "./Resources//IndiaStateCode.csv"
    STATE_CODE_WRONG_CSV_FILE_PATH = ".//home//IndiaStateCode.csv"
    STATE_CODE_WRONG_DELIMITER_FILE = ".//Resources//StateCodeWrongDelimiter.csv"
    STATE_CODE_WRONG_EXTENSION_FILE = ".//Resources//IndiaStateCode.txt"
    STATE_CODE_WRONG_HEADER_FILE = ".//Resources//StateCodeWrongHeader.csv"

    US_CENSUS_CSV_FILE_PATH = ".//Resources//USCensusFile.csv"

    def test_given_indian_census_CSV_file_returns_correct_records(self):
        analyser = Analyser()
        census_num_of_records = analyser.load_census_data(
                        TestCensusAnalyser.INDIA_CENSUS_CSV_FILE_PATH, CSVStateCensus)
        state_code_num_of_records = analyser.load_census_data(
                        TestCensusAnalyser.STATE_CODE_CSV_FILE_PATH, CSVStates)
        assert census_num_of_records == 29
        assert state_code_num_of_records == 37

    def test_given_file_with_wrong_path_should_throw_exception(self):
        try:
            analyser = Analyser()
            census_num_of_records  = analyser.load_census_data(
                            TestCensusAnalyser.INDIA_CENSUS_WRONG_CSV_FILE_PATH, CSVStateCensus)
            state_code_num_of_records = analyser.load_census_data(
                            TestCensusAnalyser.STATE_CODE_WRONG_CSV_FILE_PATH, CSVStates)
        except AnalyserError as exception:
            assert exception.exception_type == AnalyserError.ExceptionType.FILE_NOT_FOUND

    def test_given_file_with_wrong_delimiter_should_throw_exception(self):
        try:
            analyser = Analyser()
            census_num_of_records  = analyser.load_census_data(
                            TestCensusAnalyser.CENSUS_WRONG_DELIMITER_FILE, CSVStateCensus)
            state_code_num_of_records = analyser.load_census_data(
                            TestCensusAnalyser.STATE_CODE_WRONG_DELIMITER_FILE, CSVStates)
        except AnalyserError as exception:
            assert exception.exception_type == AnalyserError.ExceptionType.WRONG_DELIMITER

    def test_given_file_with_wrong_extension_should_throw_exception(self):
        try:
            analyser = Analyser()
            census_num_of_records  = analyser.load_census_data(
                            TestCensusAnalyser.INDIA_CENSUS_WRONG_EXTENSION_FILE, CSVStateCensus)
            state_code_num_of_records = analyser.load_census_data(
                            TestCensusAnalyser.STATE_CODE_WRONG_EXTENSION_FILE, CSVStates)
        except AnalyserError as exception:
            assert exception.exception_type == AnalyserError.ExceptionType.WRONG_EXTENSION

    def test_given_file_with_wrong_header_should_throw_exception(self):
        try:
            analyser = Analyser()
            census_num_of_records  = analyser.load_census_data(
                            TestCensusAnalyser.INDIA_CENSUS_WRONG_HEADER_FILE, CSVStateCensus)
            state_code_num_of_records = analyser.load_census_data(
                            TestCensusAnalyser.STATE_CODE_WRONG_HEADER_FILE, CSVStates)
        except AnalyserError as exception:
            assert exception.exception_type == AnalyserError.ExceptionType.WRONG_HEADER

    def test_given_indian_census_CSV_file_returns_statewise_sorted_data(self):
        analyser = Analyser()
        analyser.load_census_data(TestCensusAnalyser.INDIA_CENSUS_CSV_FILE_PATH, CSVStateCensus)
        sorted_json_data = analyser.get_statewise_sorted_data()
        sorted_data = list(json.loads(sorted_json_data))
        assert sorted_data[0] == "Andhra Pradesh"
        assert sorted_data[-1] == "West Bengal"

    def test_given_indian_census_CSV_file_returns_populationwise_sorted_data(self):
        analyser = Analyser()
        analyser.load_census_data(TestCensusAnalyser.INDIA_CENSUS_CSV_FILE_PATH, CSVStateCensus)
        sorted_json_data = analyser.get_populationwise_sorted_data()
        sorted_data = list(json.loads(sorted_json_data))
        assert sorted_data[0] == "Uttar Pradesh"
        assert sorted_data[-1] == "Sikkim"
    
    def test_given_state_code_CSV_file_returns_state_code_wise_sorted_data(self):
        analyser = Analyser()
        analyser.load_census_data(TestCensusAnalyser.STATE_CODE_CSV_FILE_PATH, CSVStates)
        sorted_json_state_data = analyser.get_state_code_wise_sorted_data()
        sorted_data = list(json.loads(sorted_json_state_data))
        assert sorted_data[0] == "Andhra Pradesh New"
        assert sorted_data[-1] == "West Bengal"

    def test_given_indian_census_CSV_file_returns_population_densitywise_sorted_data(self):
        analyser = Analyser()
        analyser.load_census_data(TestCensusAnalyser.INDIA_CENSUS_CSV_FILE_PATH, CSVStateCensus)
        sorted_json_data = analyser.get_population_densitywise_sorted_data()
        sorted_data = list(json.loads(sorted_json_data))
        assert sorted_data[0] == "Bihar"
        assert sorted_data[-1] == "Arunachal Pradesh"

    def test_given_indian_census_CSV_file_returns_areawise_sorted_data(self):
        analyser = Analyser()
        analyser.load_census_data(TestCensusAnalyser.INDIA_CENSUS_CSV_FILE_PATH, CSVStateCensus)
        sorted_json_data = analyser.get_areawise_sorted_data()
        sorted_data = list(json.loads(sorted_json_data))
        assert sorted_data[0] == "Rajasthan"
        assert sorted_data[-1] == "Goa"

    def test_given_us_census_CSV_file_returns_correct_records(self):
        analyser = Analyser()
        census_num_of_records = analyser.load_census_data(
                            TestCensusAnalyser.US_CENSUS_CSV_FILE_PATH, USCensusCSV)                      
        assert census_num_of_records == 51
        
    def test_given_us_census_CSV_file_returns_populationwise_sorted_data(self):
        analyser = Analyser()
        analyser.load_census_data(TestCensusAnalyser.US_CENSUS_CSV_FILE_PATH, USCensusCSV)
        sorted_json_data = analyser.get_us_populationwise_sorted_data()
        sorted_data = list(json.loads(sorted_json_data))
        assert sorted_data[0] == "California"
        assert sorted_data[-1] == "Wyoming"

    def test_given_us_census_CSV_file_returns_areawise_sorted_data(self):
        analyser = Analyser()
        analyser.load_census_data(TestCensusAnalyser.US_CENSUS_CSV_FILE_PATH, USCensusCSV)
        sorted_json_data = analyser.get_us_areawise_sorted_data()
        sorted_data = list(json.loads(sorted_json_data))
        assert sorted_data[0] == "Alaska"
        assert sorted_data[-1] == "District of Columbia"

    def test_given_us_census_CSV_file_returns_population_densitywise_sorted_data(self):
        analyser = Analyser()
        analyser.load_census_data(TestCensusAnalyser.US_CENSUS_CSV_FILE_PATH, USCensusCSV)
        sorted_json_data = analyser.get_us_population_densitywise_sorted_data()
        sorted_data = list(json.loads(sorted_json_data))
        assert sorted_data[0] == "District of Columbia"
        assert sorted_data[-1] == "Alaska"
