
"""
"""

"""
Write a program that uses simple inheritence between classes Base and Derived. If there is a method
in Base class, how do you prevent it from being overriden in the Derived Class.
"""

class Base:

    def __method(self):
        print('Base')

    def show(self):
        self.__method()


class Dervied(Base):

    def __method(self):
        print('Derived')
b = Base()
b.show()
d = Dervied()
d.show()
print(Dervied.__mro__)



"""
You are correct that in Python, when an attribute or method is accessed on an 
instance of a class, the interpreter first looks for that attribute or method 
in the derived class. If it's not found, then it looks for it in the base class 
or any other ancestor classes.

However, this behavior applies to public attributes and methods, not to private ones. 
Private attributes and methods, which are denoted by names beginning with double 
underscores (__), undergo name mangling to avoid conflicts with other classes. 
This means that their names are modified to include the class name as a prefix.

In your code, the private method __method() in the Base class is name-mangled to 
_Base__method(). Similarly, the private method __method() in the Derived class is 
name-mangled to _Derived__method().

Since these private methods have different mangled names, they are treated as 
separate methods, even though they have the same original names. When you call 
the show() method on an instance of the Derived class, it internally calls the 
mangled method name _Base__method() from the Base class, not the mangled method 
name _Derived__method().

In other words, the private methods in the Base and Derived classes are distinct 
and independent, and they are not considered as overrides of each other. The name 
mangling mechanism ensures that private methods are encapsulated within their 
respective classes and are not accessible or overridden by other classes.

So, in your code, the private method in the Base class is not being overridden by 
the private method in the Derived class because their mangled names are different. 
As a result, when you call the show() method on the Derived instance, it executes 
1the private method from the Base class and prints 'Base'.
"""

