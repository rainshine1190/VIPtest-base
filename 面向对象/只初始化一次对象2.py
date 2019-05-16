#coding:utf-8

class Dog(object):

    __instance = None
    __init_flag = False
    def __new__(cls,name):
        if cls.__instance == None:
            cls.__instance = object.__new__(cls)
            return cls.__instance
        else:
            return cls.__instance

    def __init__(self,name):
        if Dog.__init_flag == False:
            self.name = name
            Dog.__init_flag = True


d1 = Dog('旺财')
print(id(d1))
print(d1.name)

d2 = Dog('哮天犬')
print(id(d2))
print(d2.name)
