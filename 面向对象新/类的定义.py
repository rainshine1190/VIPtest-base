
#1-定义一个类
class Washer():

    #属性

    #方法
    def wash(self):
        print(self)
        print('我会洗⾐衣服')


#2-创建对象:对象名 = 类名()
haier1 = Washer()

#3-调用类中的方法：对象名.方法名()
haier1.wash()

print(haier1)

haier2 = Washer()

print(haier2)
haier2.wash()