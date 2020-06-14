import enum

class MoodAnalysisError(Exception):
    class ExceptionType(enum.Enum):
        EMPTY = 1
        NONE = 2


    def __init__(self, exception_type, message):
        super().__init__(message)
        self.exception_type = exception_type

