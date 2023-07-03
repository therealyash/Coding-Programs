
"""

"""
"""
Define a class Shape. Inherittwo classes Circle & Rectangle. Check programmatically the inheritence
relationship between the classes. Create Shape and Cirlce objects. Report of which classes are these
objects instances of.
"""

class Shape:
    pass

class Circle(Shape):

    def show(self):
        print('Circle')

class Rectangle(Shape):

    def show(self):
        print('Rectangle')


s = Shape()
c = Circle()
print(isinstance(s,Shape))
print(isinstance(s,Rectangle))
print(isinstance(s,Circle))
print(issubclass(Rectangle, Shape))
print(issubclass(Circle, Shape))








