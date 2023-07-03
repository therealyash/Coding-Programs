
from abc import ABC, abstractmethod
class Character(ABC):

    @abstractmethod
    def patriotism(self):
        pass

class Actor:
    def style(self):
        print('Actor Style!')

class Person(Character, Actor):

    def patriotism(self):
        print('Patriotism!')

    def style(self):
        print('Person Style!')

    def do_acting(self):
        print('Do acting!')

p = Person()
p.patriotism()
p.style()
p.do_acting()









