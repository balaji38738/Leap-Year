from abc import ABC, abstractmethod

class StateDAOInterface(ABC):
    @abstractmethod
    def get(self, state_name):
        pass

    @abstractmethod
    def get_all(self):
        pass