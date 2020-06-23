import pandas as pd
import icsv_builder
import csv
from census_analyser_exception import AnalyserError
from csv_state_census import CSVStateCensus
from csv_states import CSVStates
import os

class CSVBuilder(icsv_builder.ICSVBuilder):
    def load_csv_data(self, csv_file_path, class_name):
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
            data_frame = pd.read_csv(
                    csv_file_path,
                    index_col=None,
                    sep=",",
                    usecols=class_name.get_headers())
            return data_frame
        except FileNotFoundError:
            raise AnalyserError(AnalyserError.ExceptionType.FILE_NOT_FOUND, "File not found")
        except ValueError:
            raise AnalyserError(AnalyserError.ExceptionType.WRONG_DELIMITER,
                                    "File should have comma delimiter")
