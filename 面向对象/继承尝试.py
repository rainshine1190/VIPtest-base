

class A():

    def __init__(self,a,*args):
        self.a = a

    def A1(self):
        print('A1方法')


class B(A):

    def __init__(self,a,name):
        self.name = name
        super(B, self).__init__(a)

    def B1(self):
        print('B1方法')
        self.A1()
        print(self.a)

    def __str__(self):
        return f'我是对象{self.name}'

b = B(1,'xm')
print(b)
b.B1()