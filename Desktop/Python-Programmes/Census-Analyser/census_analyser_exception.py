import enum

class AnalyserError(Exception):
    class ExceptionType(enum.Enum):
        FILE_NOT_FOUND = 1
        WRONG_DELIMITER = 2
        WRONG_EXTENSION = 3
        WRONG_HEADER = 4

    def __init__(self, exception_type, message):
        self.message = message
        self.exception_type = exception_type
        super().__init__(self.message)