import pandas as pd

class CSVDataLoader:
    @staticmethod
    def load_csv_data(csv_file_path, class_name):
        data_frame = pd.read_csv(
                csv_file_path,
                index_col=None,
                sep=",",
                usecols=class_name.get_headers())
        return data_frame