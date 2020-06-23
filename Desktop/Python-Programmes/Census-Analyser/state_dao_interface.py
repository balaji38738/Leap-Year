from abc import abstractmethod

class StateDAOInterface:
    @abstractmethod
    def get(self, state_name):
        pass

    @abstractmethod
    def get_all(self):
        pass