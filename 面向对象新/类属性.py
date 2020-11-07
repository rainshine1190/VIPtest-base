

'''

类属性


'''


class A():
    name = 'a'

    def __init__(self):
        self.age = 12

    @classmethod
    def func1(cls):
        print('类方法引用类属性',cls.name)

    def func2(self):
        print('实例方法引用类属性',self.name)



a = A()
print(a.name)