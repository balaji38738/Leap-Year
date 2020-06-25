import csv
from census_analyser_exception import AnalyserError
from csv_state_census import CSVStateCensus
from csv_states import CSVStates
import os
from csv_builder_factory import CSVBuilderFactory
import json

class Analyser:
    
    # Method to load India census csv data and count entries
    def load_census_data(self, csv_file_path, class_name):
        self.csv_builder_obj = CSVBuilderFactory.create_csv_builder()
        self.state_dataframe = self.csv_builder_obj.load_csv_data(csv_file_path, class_name)
        self.headers = list(self.state_dataframe.columns)
        return self.state_dataframe.shape[0]

    # Returns the state data sorted in lexicographical order of state name in json format
    def get_statewise_sorted_data(self):
        return self.sort(self.headers[0], True, self.headers[0])

    #   Returns the state data sorted in descending order of population
    def get_populationwise_sorted_data(self):
        return self.sort(self.headers[1], False, self.headers[0])

    #   Returns the state data sorted in lexicographical order of state code in json format
    def get_state_code_wise_sorted_data(self):
        return self.sort(self.headers[3], True, self.headers[1])

    #   Returns the state data sorted in descending order of population density
    def get_population_densitywise_sorted_data(self):
        return self.sort(self.headers[3], False, self.headers[0])

    #   Returns the state data sorted in descending order of state area
    def get_areawise_sorted_data(self):
        return self.sort(self.headers[2], False, self.headers[0])

    #   Returns the us state data sorted in descending order of population
    def get_us_populationwise_sorted_data(self):
        return self.sort(self.headers[2], False, self.headers[1])

    #   Returns the state data sorted in descending order of state area
    def get_us_areawise_sorted_data(self):
        return self.sort(self.headers[4], False, self.headers[1])

    def sort(self, sort_by, ascending_, index_col):
        sorted_data = self.state_dataframe.sort_values(by=sort_by, ascending=ascending_)
        sorted_data = sorted_data.set_index(index_col).T.to_dict('list')
        json_data = json.dumps(sorted_data)
        return json_data