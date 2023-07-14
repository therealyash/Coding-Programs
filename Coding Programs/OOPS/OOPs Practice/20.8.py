from abc import ABC, abstractmethod

class A(ABC):

    @abstractmethod
    def A(self):
        pass

class B(A):
    pass
    # def A(self):
    #     print('A')

b = B()
b.A()







