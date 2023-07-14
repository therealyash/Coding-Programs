
from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def speed(self):
        print('Speed')

    @abstractmethod
    def maintenance(self):
        print('Maintenance')

    @abstractmethod
    def value(self):
        print('Value')


class FourWheeler(Vehicle):
    pass

class TwoWheeler(Vehicle):
    pass

class Airborne(Vehicle):
    pass

f = FourWheeler()
f.speed()




