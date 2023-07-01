

"""
Method Overloading
"""

"""
Polymorphism can be achieved by 2 ways - 1. Method Overloading 2. Method Overriding

Method Overloading
Same method defined multiple times in the same class with different parameters
then it is called Method Overloading.

Even 1 function can have different forms in Method Overloading.

"""

class A:

    def show(self):
        print('Welcome!')

    def show(self, Firstname=''):
        print('Welcome,', Firstname)

    def show(self, Firstname='', Lastname=''):
        print('Welcome,',Firstname, Lastname)

a = A()
a.show('Yashraj', 'Limkar')





