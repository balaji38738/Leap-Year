from mood_analyser import MoodAnalyser, FileHandler
from mood_analysis_error import MoodAnalysisError

class MoodAnalyserFactory:
    @staticmethod
    def get_mood_analyser_object(class_name):
        if (class_name == "MoodAnalyser"):
            moood_analyser_obj = MoodAnalyser()
            return moood_analyser_obj
        else:
            raise MoodAnalysisError(MoodAnalysisError.ExceptionType.CLASS_NOT_FOUND, "Class not found")

messages = FileHandler().read_file("messages.json")
for message in messages:
    mood_analyser = MoodAnalyserFactory.get_mood_analyser_object("MoodAnalyser")
    mood = mood_analyser.analyse_mood(message["message"])
    print(mood)

try:
    obj = MoodAnalyserFactory.get_mood_analyser_object("mood_analyser")
except MoodAnalysisError:
    print("Class Not Found")

# mood_obj = MoodAnalyser()
# print(mood_obj.analyse_mood("I am sad"))
# mood_obj2 = MoodAnalyser("I am happy")
# print(mood_obj2.analyse_mood())