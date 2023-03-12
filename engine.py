from abc import ABC, abstractmethod
from car import Car

class Engine(Car, ABC):
    @abstractmethod
    def needs_service(self):
        pass
