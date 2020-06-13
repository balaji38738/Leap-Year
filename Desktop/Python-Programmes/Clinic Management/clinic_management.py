import json

class FileReader:
    def __init__(self, file_path):
        with open(file_path) as doctor_file:
            self.file_data = json.load(doctor_file)

doctor_data = FileReader("doctor_data.json")