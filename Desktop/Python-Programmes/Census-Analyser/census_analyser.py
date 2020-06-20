import pandas as pd
import csv
from census_analyser_exception import CensusAnalyserError
from csv_state_census import CSVStateCensus
from csv_states import CSVStates
import os

class CensusAnalyser:
    
    # Method to load India census csv data and count entries
    def load_india_census_data(self, csv_file_path, class_name):
        filename, extension = os.path.splitext(csv_file_path)
        if extension != ".csv":
            raise CensusAnalyserError(CensusAnalyserError.ExceptionType.WRONG_EXTENSION,
                                    "File should be csv file")
        try:                           
            with open(csv_file_path) as csv_file:
                reader = csv.reader(csv_file)
                headers = next(reader)
        except FileNotFoundError:
            raise CensusAnalyserError(CensusAnalyserError.ExceptionType.FILE_NOT_FOUND,
                                    "File not found")
        if headers != class_name.get_headers():
            raise CensusAnalyserError(CensusAnalyserError.ExceptionType.WRONG_HEADER,
                                    "csv file has wrong headers")
        try:
            india_census = pd.read_csv(
                        csv_file_path,
                        index_col=None,
                        sep=",",
                        usecols=class_name.get_headers())
            return india_census.shape[0]
        except FileNotFoundError:
            raise CensusAnalyserError(CensusAnalyserError.ExceptionType.FILE_NOT_FOUND,
                                    "File not found")
        except ValueError:
            raise CensusAnalyserError(CensusAnalyserError.ExceptionType.WRONG_DELIMITER,
                                    "File should have comma delimiter")
