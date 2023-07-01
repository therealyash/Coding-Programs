# Inheritence
# Used when 2 classes have a 'like a' relationship
# 'like a' for example means - Button is like a window. So Button can inherit features of window
# A child or sub class is derieved from a parent or base class

# base class or parent class
class Index:

    def __init__(self):
        self._count = 0

    def display(self):
        print('count = ' + str(self._count))

    def incr(self):
        self._count += 1

# derieved class or child class
class NewIndex(Index):

    def __init__(self):
        super().__init__()

    def decr(self):
        self._count -= 1

i = NewIndex()
i.incr()
i.incr()
i.incr()
i.display()
i.decr()
i.display()
i.decr()
i.display()

# isinstance(o,c)
# isinstance(o,c) is used to check whether an object o is an instance of a class c

# issubclass
# is subclass(d,b) is used to check whether class d has been derived from class b


# SUPPRESSING FEATURE
# Supressing an existing feature: To implement this just establish class implementation by defining same method in derived class
class A:

    def __init__(self, a):
        self._a = a

    def display(self):
        print(self._a)

    def lol(self):
        print("Lol!")

class B(A):

    def __init__(self, b):
        super().__init__(7)
        self._b = b

    def display(self):
        print("Faking method")
        super().lol()           # using super to call base_class_method()
        A.lol(self)             # using Class name to call base_class_method()

b = B(8)
b.display()

"""
Extending an existing feature - To implement this, call base class method from derived class
by using one of the following two forms

super().base_class_method()
Baseclassname.base_class_method(self)
"""

"""
Types of Inheritence:

a. Simple Inheritence - B derived from A
b. Multi Level Inheritence - Ex class HOD is derived from class Professor which is derived form class Person
c. Multiple Inheritence - Ex class HardwareSales derived from 2 base classes - Product & Sales00000000000000000000
"""


