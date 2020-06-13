import json


class FileHandler:
    """Reads and writes files of clinique"""

    def read_file(self, file_path):
        with open(file_path) as clinique_file:
            file_data = json.load(clinique_file)
            return file_data

    def write_file(self, file_path, new_entry):
        file_data = self.read_file(file_path)
        with open(file_path, "w") as clinique_file:
            file_data.append(json.dumps(new_entry))
            json.dump(file_data, clinique_file, indent=4)


class CliniqueManagement:
    def __init__(self):
        self.file_hanler = FileHandler()
        self.doctor_data = self.file_hanler.read_file("doctor_data.json")

    def search_doctor(self, key):
        for doctor in self.doctor_data:
            if ((doctor["Doctor Name"] == key)
                    or (doctor["Doctor Id"] == key)):
                return doctor