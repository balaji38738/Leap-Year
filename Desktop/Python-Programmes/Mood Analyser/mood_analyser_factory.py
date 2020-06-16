from mood_analyser import MoodAnalyser
from mood_analysis_error import MoodAnalysisError

class MoodAnalyserFactory:
    @staticmethod
    def get_mood_analyser_object(class_name):
        if (class_name == "MoodAnalyser"):
            moood_analyser_obj = MoodAnalyser()
            return moood_analyser_obj
        else:
            raise MoodAnalysisError(MoodAnalysisError.ExceptionType.CLASS_NOT_FOUND, "Class not found")