"""
功能描述：
编写人：
编写日期：
实现逻辑：

"""
#创建类
class Washer():

    #方法
    def wash(self):
        # print(self)
        print('类里面获取对象的属性',self.height)
        print('洗衣服')

#创建对象
w1 = Washer()
w2 = Washer()


print('w1对象的内容',w1)
print('w2对象的内容',w2)
#对象调用类中的方法
# w1.wash()
# w2.wash()

#类的外面添加对象属性
w1.height = 100
w1.wash()
w2.wash()
#获取对象属性
print('类外面获取对象属性',w1.height)
