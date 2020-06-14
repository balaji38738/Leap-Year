import json

class FileHandler:
    def read_file(self, file_path):
        with open(file_path) as message_file:
            messages = json.load(message_file)
        return messages


class MoodAnalyser:
    def analyse_mood(self, message):
        if message.find("happy") != -1:
            return "happy"
        elif message.find("sad") != -1:
            return "sad"
        else:
            return "Invalid mood"


messages = FileHandler().read_file("messages.json")
mood_analyser = MoodAnalyser()
for message in messages:
    mood = mood_analyser.analyse_mood(message["message"])
    print(mood)
