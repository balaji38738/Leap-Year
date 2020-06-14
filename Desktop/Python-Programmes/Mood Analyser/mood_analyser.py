import json

class FileHandler:
    def read_file(self, file_path):
        with open(file_path) as message_file:
            messages = json.load(message_file)
        return messages


class MoodAnalyser:
    def __init__(self, message):
        self.message = message

    def analyse_mood(self):
        if ((self.message.find("happy") != -1)
                or (self.message.find("any") != -1)):
            return "happy"
        elif self.message.find("sad") != -1:
            return "sad"
        else:
            return "Invalid mood"


messages = FileHandler().read_file("messages.json")
for message in messages:
    mood_analyser = MoodAnalyser(message["message"])
    mood = mood_analyser.analyse_mood()
    print(mood)
