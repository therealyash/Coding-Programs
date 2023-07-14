
class B1:

    def __init__(self, name):
        self.name = name
        print('Class Name:',name)

    def __del__(self):
        print('Destructor: B1')
class B2:
    def __init__(self, name):
        self.name = name
        print('Class Name:',name)

    def __del__(self):
        print('Destructor: B2')
class D(B1, B2):

    def __init__(self):
        B1.__init__(self,'B1')
        B2.__init__(self,'B2')

    def __del__(self):
        print('Destructor: D')

        B1.__del__(self)
        B2.__del__(self)



d = D()
print(isinstance(d,D))





