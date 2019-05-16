#coding:utf-8
# __author__ = 'lc'


class Dog(object):
    def print_self(self):
        print("大家好，我是xxxx")

class Xiaotq(Dog):
    def print_self(self):
        print("Hello,everybody,我是你们的老大，我是xxx")

def introduce(temp):
    temp.print_self()


dog1 = Dog()
dog2 = Xiaotq()

#多态的关键在于，同样是调用相同的方法，但是完成的内容却不同，普通狗的自我介绍是：xxx，哮天犬的自我介绍是：xxx

introduce(dog1)
introduce(dog2)