#coding:utf-8
# __author__ = 'lc'

#如果调用的是继承父类中的公有方法可以在这个公有方法中访问父类中的私有属性和私有方法
#但是如果在子类中实现了一个公有方法，那么这个方法是不能够调用继承的父类中的私有方法和私有属性的

class A:
    def __init__(self):
        self.num1 = 100
        self.__num2 = 200
        # print(self.num1,self.__num2)

    def test1(self):
        print("----公有方法")

    def __test2(self):
        print("----私有方法")

    def test3(self):
        print("----公有方法中调用私有方法和私有属性")
        self.__test2()
        print(self.num1)
        print(self.__num2)

class B(A):
    def test4(self):
        # self.__num2
        self.__test2()

b = B()
b.test4()

