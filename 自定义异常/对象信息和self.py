


class A():

    def fun(self):
        print(self)

    def __str__(self):
        return f'我是A对象信息'


a = A()
# print(a)
a.fun()