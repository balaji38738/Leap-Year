from abc import abstractmethod

class ICSVBuilder:
    @abstractmethod
    def load_csv_data(self, csv_file_path, class_name):
        pass