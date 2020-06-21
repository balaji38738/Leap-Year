import csv
from census_analyser_exception import AnalyserError
from csv_state_census import CSVStateCensus
from csv_states import CSVStates
import os
from csv_builder_factory import CSVBuilderFactory
import json

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
                self.headers = next(reader)
            if self.headers != class_name.get_headers():
                raise AnalyserError(AnalyserError.ExceptionType.WRONG_HEADER,
                                        "csv file has wrong headers")
            self.csv_builder_obj = CSVBuilderFactory.create_csv_builder()
            self.state_dataframe = self.csv_builder_obj.load_csv_data(csv_file_path, class_name)
            return self.state_dataframe.shape[0]
        except FileNotFoundError:
            raise AnalyserError(AnalyserError.ExceptionType.FILE_NOT_FOUND, "File not found")
        except ValueError:
            raise AnalyserError(AnalyserError.ExceptionType.WRONG_DELIMITER,
                                    "File should have comma delimiter")

    #   Returns the state data sorted in lexicographical order of state name in json format
    def get_statewise_sorted_data(self):
        sorted_data = self.state_dataframe.sort_values(by=[self.headers[0]])
        json_data = sorted_data.to_json(orient="records")
        return json_data

    #   Returns the state data sorted in lexicographical order of state code in json format
    def get_state_code_wise_sorted_data(self):
        sorted_data = self.state_dataframe.sort_values(by=[self.headers[3]])
        json_data = sorted_data.to_json(orient="records")
        return json_data