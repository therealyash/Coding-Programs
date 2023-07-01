# Practice & Revision Program for Classes

class Car:

    # static variable
    wheels = 4

    def __init__(self, company, model, color, engineCC):

        # instance variables
        self.__company = company # private
        self._model = model     # protected
        self.color = color     # public
        self.engineCC = engineCC

    def __str__(self):
        return f"Company:{self.__company}, Model:{self._model}, Color:{self.color}"

    # __dundermethods
    def __eq__(self, other):
        if self.engineCC == other.engineCC:
            return "Power is Same!"
        else:
            return "Power not Same!"


a = Car("BMW", "M3", "Cyan", 2400)
b = Car("Audi", "A4", "White", 2400)
print(a)
print(b)
print(a.wheels)
print(b.wheels)
print(a==b)
print(type(a))
print(vars(a))
print(dir(Car))



