import csv
from census_analyser_exception import AnalyserError
from csv_state_census import CSVStateCensus
from csv_states import CSVStates
import os
from csv_data_loader import CSVDataLoader

class Analyser:
    
    # Method to load India census csv data and count entries
    def analyse_csv_data(self, csv_file_path, class_name):
        filename, extension = os.path.splitext(csv_file_path)
        if extension != ".csv":
            raise AnalyserError(AnalyserError.ExceptionType.WRONG_EXTENSION,
                                    "File should be csv file")
        try:                           
            with open(csv_file_path) as csv_file:
                reader = csv.reader(csv_file)
                headers = next(reader)
            if headers != class_name.get_headers():
                raise AnalyserError(AnalyserError.ExceptionType.WRONG_HEADER,
                                        "csv file has wrong headers")
            india_census = CSVDataLoader.load_csv_data(csv_file_path, class_name)
            return india_census.shape[0] 
        except FileNotFoundError:
            raise AnalyserError(AnalyserError.ExceptionType.FILE_NOT_FOUND, "File not found")
        except ValueError:
            raise AnalyserError(AnalyserError.ExceptionType.WRONG_DELIMITER,
                                    "File should have comma delimiter")
