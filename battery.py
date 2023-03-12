from abc import ABC, abstractmethod
from car import Car

class Battery(Car, ABC):
    @abstractmethod
    def needs_service(self):
        pass
