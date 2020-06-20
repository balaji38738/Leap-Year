import pandas as pd
from census_analyser_exception import AnalyserError
from header import Header

class CSVStateCensus(Header):
    @staticmethod
    def get_headers():
        return ['State', 'Population', 'AreaInSqKm', 'DensityPerSqKm']
