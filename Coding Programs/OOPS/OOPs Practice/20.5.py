

class B:

    def b1(self):
        print('B1')

    def __b2(self):
        print('B2')

class D(B):

    def d1(self):
        print('D1')

    def d2(self):
        print('D2')
        b = B()
        b.b1()
        #b.b2()


d = D()
d.d2()






