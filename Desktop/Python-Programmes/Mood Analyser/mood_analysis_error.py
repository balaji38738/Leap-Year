import enum

class MoodAnalysisError(Exception):
    class ExceptionType(enum.Enum):
        EMPTY = 1
        NONE = 2
        CLASS_NOT_FOUND = 3


    def __init__(self, exception_type, message):
        self.message = message
        super().__init__(self.message)
        self.exception_type = exception_type

