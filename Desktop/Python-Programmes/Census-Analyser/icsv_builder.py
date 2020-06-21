from abc import abstractstaticmethod

class ICSVBuilder:
    @abstractstaticmethod
    def load_csv_data(csv_file_path, class_name):
        pass