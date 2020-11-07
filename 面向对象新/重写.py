'''





'''


class A():

    def __init__(self):
        self.name = 1

    def func(self):
        print('funca')


class B(A):

    def __init__(self):
        self.name = 2

    def func(self):
        print('funcb')

    def abc(self):
        super().__init__()
        super().func()

b = B()
b.abc()