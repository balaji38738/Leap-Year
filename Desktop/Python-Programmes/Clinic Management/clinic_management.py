import json

class FileHandler:
    def read_file(self, file_path):
        with open(file_path) as clinique_file:
            file_data = json.load(clinique_file)
            return file_data

    def write_file(self, file_path, new_entry):
        file_data = self.read_file(file_path)
        with open(file_path, "w") as clinique_file:
            file_data.append(json.dumps(new_entry))
            json.dump(file_data, clinique_file, indent=4)


file_hanler = FileHandler()
doctor_data = file_hanler.read_file("doctor_data.json")
print(doctor_data)
patient = {"Patient Name": "Mahesh Munde", "Id": 1, "Mobile": 7588842796, "Age": 24}
file_hanler.write_file("patient_data.json", patient)
patient_data = file_hanler.read_file("patient_data.json")
print(patient_data)