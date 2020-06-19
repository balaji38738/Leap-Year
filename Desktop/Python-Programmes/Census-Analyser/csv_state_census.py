import pandas as pd
from census_analyser_exception import CensusAnalyserError

class CSVStateCensus:
    @staticmethod
    def get_census_headers():
        return ['State', 'Population', 'AreaInSqKm', 'DensityPerSqKm']
