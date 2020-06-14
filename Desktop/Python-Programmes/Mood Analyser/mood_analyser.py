import json

class FileHandler:
    def read_file(self, file_path):
        with open(file_path) as moods_file:
            moods = json.load(moods_file)
        return moods


class MoodAnalyser:
    def __init__(self, file_path):
        self.file_handler = FileHandler()
        self.moods = self.file_handler.read_file(file_path)

    def analyse_mood(self, message):
        if message.find(self.moods[0]["mood"]) != -1:
            return "happy"
        elif message.find(self.moods[1]["mood"]) != -1:
            return "sad"
        else:
            return "Invalid mood"

mood_analyser = MoodAnalyser("moods.json")
print(mood_analyser.analyse_mood("I am happy"))
print(mood_analyser.analyse_mood("I am sad"))  
print(mood_analyser.analyse_mood("I am angry"))     
