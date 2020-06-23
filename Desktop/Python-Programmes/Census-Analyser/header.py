from abc import ABC, abstractstaticmethod

class Header(ABC):
    @abstractstaticmethod
    def get_headers():
        pass