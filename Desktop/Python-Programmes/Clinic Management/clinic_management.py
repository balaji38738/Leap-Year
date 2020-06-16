import json
import re

class Time:
    time_pattern = r"[0-9]{2}:[0-9]{2}"

    # Validates a formatted time string
    @classmethod
    def validate_time(cls, time):
        if re.match(cls.time_pattern, time):
            hours, minutes = [int(time_element) for time_element in input().split(":")]
            return (hours >=0 and hours <= 23) and (minutes >= 0 and minutes <= 59)
        return False

    # Checks if given time is in between other two times       
    @staticmethod
    def is_in_interval(start_time, end_time, check_time):
        return (check_time > start_time) and (check_time < end_time)


class FileHandler:
    """Reads and writes files of clinique"""

    # Returns python object of json data from given file path
    def read_file(self, file_path):
        with open(file_path) as clinique_file:
            file_data = json.load(clinique_file)
            return file_data

    # Writes python object in given json file path
    def write_file(self, file_path, new_entry):
        file_data = self.read_file(file_path)
        with open(file_path, "w") as clinique_file:
            file_data.append(json.dumps(new_entry))
            json.dump(file_data, clinique_file, indent=4)


class CliniqueManagement:
    def __init__(self):
        self._file_hanler = FileHandler()
    
    # Returns list of search results given searching file, searching keyword & key 
    def search(self, search_file, search_by, key):
        search_list = self._file_hanler.read_file(search_file)
        search_results = []
        for element in search_list:
            if search_by == "Availabilty":
                if not self.get_doctor_if_available(element, key):
                    search_results.append(element)
            elif isinstance(key, int):
                if element[search_by] == key:
                    search_results.append(element)
            elif element[search_by].find(key) != -1:
                search_results.append(element)
        return search_results

    # Returns the doctor if available
    def get_doctor_if_available(self, doctor, time):
        search_results = []
        for time_frame in doctor["Availabilty"]:
            if (Time.is_in_interval(time_frame["Start Time"],
                    time_frame["End Time"], time)):
                search_results.append(doctor)


file_handler = FileHandler()
patient = {"Name": "First Patient", "Id": 1, "Mobile": 1234567890, "Age": 20}
file_handler.write_file("patient_data.json", patient)