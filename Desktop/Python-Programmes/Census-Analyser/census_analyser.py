import pandas as pd
from census_analyser_exception import CensusAnalyserError
from csv_state_census import CSVStateCensus

class CensusAnalyser:
    
    # Method to load csv data and count entries
    def load_india_census_data(self, csv_file_path):
        try:
            india_census = pd.read_csv(
                        csv_file_path,
                        index_col=None,
                        sep=",",
                        usecols=CSVStateCensus.get_census_headers())
            return india_census.shape[0]
        except FileNotFoundError:
            raise CensusAnalyserError(CensusAnalyserError.ExceptionType.FILE_NOT_FOUND,
                                    "File not found")
        except ValueError:
            raise CensusAnalyserError(CensusAnalyserError.ExceptionType.WRONG_DELIMITER,
                                    "File should have comma delimiter")
