import pandas as pd

class CensusAnalyser:
    
    # Method to load csv data and count entries
    def load_india_census_data(self, csv_file_path):
        india_census = pd.read_csv(csv_file_path, index_col=None)
        return len(india_census)