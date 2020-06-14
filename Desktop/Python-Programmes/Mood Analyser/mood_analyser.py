import json

class FileHandler:
    def read_file(self, file_path):
        with open(file_path) as moods_file:
            moods = json.load(moods_file)
        return moods

file_handler = FileHandler()
print(file_handler.read_file("moods.json"))