#coding:utf-8
__author__ = 'lc'



class Dog():
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance == None:
            cls.__instance = object.__new__(cls)
            return cls.__instance
        else:
            return cls.__instance


d1 = Dog()
d2 = Dog()

print(id(d1))
print(id(d2))









