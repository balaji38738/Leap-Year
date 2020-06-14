import json
import re

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

    def search_doctor_by_name(self, name):
        relevant_doctors = []
        for doctor in self.doctor_data:
            if doctor["Doctor Name"].find(name) != -1:
                relevant_doctors.append(doctor)
        return relevant_doctors

    def search_doctor_by_specialisation(self, specialisation):
        relevant_doctors = []
        for doctor in self.doctor_data:
            if doctor["Specialisation"].find(specialisation) != -1:
                relevant_doctors.append(doctor)
        return relevant_doctors
    
    def search_doctor_by_id(self, id):
        for doctor in self.doctor_data:
            if doctor["Doctor Id"].find(id) != -1:
                return doctor
                