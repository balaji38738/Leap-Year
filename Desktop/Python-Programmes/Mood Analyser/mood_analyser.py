import json
from mood_analysis_error import MoodAnalysisError

class FileHandler:
    def read_file(self, file_path):
        with open(file_path) as message_file:
            messages = json.load(message_file)
        return messages


class MoodAnalyser:
    def __init__(self, message=""):
        self.message = message

    def analyse_mood(self, message=""):
        if self.message == "":
            self.message = message
        try:
            if self.message == "":
                raise MoodAnalysisError(MoodAnalysisError.ExceptionType.EMPTY, "Please provide mood")
            elif ((self.message.find("happy") != -1)
                    or (self.message.find("any") != -1)):
                return "happy"
            elif self.message.find("sad") != -1:
                return "sad"
            else:
                return "Invalid mood"
        except AttributeError:
            raise MoodAnalysisError(MoodAnalysisError.ExceptionType.NONE, "Invalid message")