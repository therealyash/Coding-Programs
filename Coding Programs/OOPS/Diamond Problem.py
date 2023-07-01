# Diamond Problem

class Base:

    def display(self):
        print('In Base!')

class Derived1(Base):

    def display(self):
        print('In Derived 1')

class Derived2(Base):

    def display(self):
        print('In Derived 2')

class Der(Derived1, Derived2):

    def display(self):
        super().display()
        Derived1.display(self)
        Derived2.display(self)
        print(Der.__mro__)

d1 = Der()
d1.display()
