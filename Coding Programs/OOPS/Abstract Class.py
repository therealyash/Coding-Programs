

"""
Abstract Class

-A class from which an object cannot be created is called an abstract class
-abc is a module whichs stands for abstract base classes
-importing class ABC & decorator abstractmethod
"""


from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass

class Rectangle(Shape):
    def draw(self):
        print('In Rectangle.draw')

class Circle(Shape):
    def draw(self):
        print('In Circle.draw')

s = Shape() # will result in error as shape is an abstract class
c = Circle()
c.draw()












