from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self,brand,speed) -> None:
        super().__init__()
        self.brand = brand
        self.speed = speed
        self.gear = 0
        self.seat = 0

    @abstractmethod
    def show_detail(self):
        pass
    