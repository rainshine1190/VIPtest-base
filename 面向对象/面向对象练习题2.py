#coding:utf-8


# 2、小明爱跑步，爱吃东西。
# 1）小明体重75.0公斤
# 2）每次跑步会减肥0.5公斤
# 3）每次吃东西体重会增加1公斤
# 4）小美的体重是45.0公斤

class Person:
    def __init__(self,name,weight):
        self.name = name
        self.weight = weight

    def __str__(self):
        return ('%s的体重是%0.1f公斤'%(self.name,self.weight))

    def run(self):
        self.weight -= 0.5
        print('%s跑步减肥0.5公斤'%(self.name))

    def eat(self):
        self.weight += 1
        print('%s吃东西体重增加1公斤' % (self.name))


p = Person('小明',75)
print(p)
p.run()
print(p)

p2 = Person('小美',45)
print(p2)
p2.eat()
print(p2)

