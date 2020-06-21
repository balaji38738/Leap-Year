import csv_builder

class CSVBuilderFactory:
    @staticmethod
    def create_csv_builder():
        csv_builder_obj = csv_builder.CSVBuilder()
        return csv_builder_obj