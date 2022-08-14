"""

1、打印小猫爱吃鱼，小猫要喝水
2、小明爱跑步，爱吃东西。
1）小明体重75.0公斤
2）每次跑步会减肥0.5公斤
3）每次吃东西体重会增加1公斤
4）小美的体重是45.0公斤



"""


"""
1-类：Cat
属性：
方法：eat_fish drink_water

"""

# class Cat(object):
#
#     def eat_fish(self):
#         print('小猫爱吃鱼')
#
#     def drink_water(self):
#         print('小猫要喝水')
#
#
# tom = Cat()
# tom.eat_fish()
# tom.drink_water()


#分析：

'''
类：Person
属性：name，weight

方法：run，eat
run：weight - xx斤





'''

# class Person(object):
#
#     def __init__(self,name,weight):
#         self.name = name
#         self.weight = weight
#
#     def run(self):
#         self.weight -= 0.5
#         print(f'{self.name}跑步，体重减少了，现在重{self.weight}公斤')
#
#     def eat(self):
#         self.weight += 1
#         print(f'{self.name}吃东西，体重增加了，现在重{self.weight}公斤')
#
#     def __str__(self):
#         return f'{self.name}体重是{self.weight}公斤'
#
#
#
# p = Person('xm',75.0)
# print(p.weight)
# print(p)
# p.run()
# print(p.weight)
#
#
#
# m = Person('xh',50.0)
# m.eat()
#
#


"""
3、摆放家具
需求：
1）.房子有户型，总面积和家具名称列表
   新房子没有任何的家具
2）.家具有名字和占地面积，其中
   床：占4平米
   衣柜：占2平面
   餐桌：占1.5平米
3）.将以上三件家具添加到房子中
4）.打印房子时，要求输出:户型，总面积，剩余面积，家具名称列表


"""


'''
类：家/房子
属性：户型、面积、（剩余面积）、家具列表
方法：
    初始化
    添加家具
    __str__
    
类：家具
属性：名字、占地面积
方法：

'''
#
# class Furnicure(object):
#
#     def __init__(self,name,cover_area):
#         self.name = name
#         self.cover_area = cover_area
#
#
# class Home(object):
#
#     def __init__(self, hx, area):
#
#         self.hx = hx
#         self.area = area
#         self.jiaju_list = []
#         self.symj = self.area
#
#     def add_jiaju(self,item):
#         """往房子里添加家具，房子的面积就减少了"""
#         if self.symj >= item.cover_area:
#             self.symj = self.area - item.cover_area
#             print(f'房子添加完家具{item.name}后，剩余面积是{self.symj}')
#         else:
#             print('房子太小了，放不下了')
#
#
#
# bed = Furnicure('床',200)
# print(bed.name,bed.cover_area)
#
# house = Home('三室一厅', 120)
# print(house.hx,house.area)
#
# house.add_jiaju(bed)




"""
烤地瓜



"""
# # #定义一个类.地瓜
# class Potato(object):
#     #定义构造函数.初始化属性.  时间0,状态生的,不加调料
#     def __init__(self):
#         self.status = "生的"
#         self.time = 0
#         self.cooper = []
#
#     #定义cook烤地瓜方法.
#     def cook(self, time,cooper=''):
#         #
#         self.cooper.append(cooper)
#         self.time = self.time + time
#         if 0 <= self.time < 3:
#             self.status = "生的"
#         elif 3 <= self.time < 5:
#             self.status = "半生不熟"
#         elif 5 <= self.time < 8:
#             self.status = "熟的"
#         else:
#             self.status = "烤糊了"
#
#
#
#     def __str__(self):
#         #定义类的解释
#         return "这个地瓜考了{0}分钟,状态是{1},调料：{2}".format(self.time, self.status, self.cooper)
#
#
# p = Potato()
# print(p)
#
# p.cook(2,'孜然')
# print(p)
# p.cook(2,'辣椒')
# print(p)


# title = ["id","interfaceUrl","name","Method","value","expect","real","status"]
# case = ['1', 'https://www.wanandroid.com/user/login', 'login', 'post', "{'username':'liangchao','password':'123456'}", '0', '', '']
#
# dict1 = {title[i]:case[i] for i in range(len(title))}
# print(dict1)

# import xlrd
#
# excel = xlrd.open_workbook()
# sheet = excel.sheet_by_index()
# excel.sheet_by_name()
#
# sheet.nrows
# sheet.ncols
#
# sheet.row_values()
# sheet.col_values()
#
#
# sheet.cell_value()

# list1 = ['1','2','3']
# list2 = [3,4,5]
#
# dict1 = {list1[i]:list2[i] for i in range(len(list2))}
# print(dict1)
#



# def num1 (a,b):
#     sum = input("输入的数组：")
#     for i in sum:
#         a = b+a
#         b = a
#         a = b
#         i +=1
#         return
# num1(5)

#
# lis1 = [1,2,3,4,5,5,2,3,2,4]
#
# for i in lis1:
#     lis1.count(i)
#     lis1.pop(i)
#     lis1.sort()
# print(lis1)
# 运行结果为：
# [1, 2, 3, 4, 5]



# str ="welocme to super&Test"
# i = str.split(' ')
# str_list = []
# while(i >= 0):
#     str_list.append(str[i])
#     i = i - 1
# print(''.join(str_list))


# a =1
# b =1
# for i in range(10):
#     a ,b = b ,(a+b)
#     print(a)



# glo_list=[]
#
# def main():
#     print('----------------------------')
#     print('---1-注册；2-查询；3-退出------')
#     print('----------------------------')
#     a = int(input('请选择您要的功能：'))
#     if a == 1:
#         add_user()
#     elif a == 2:
#         panduan()
#     elif a == 3:
#         print('退出系统')
#         exit()
#     else:
#         print('请输入合法字符！')
#
#
#
# def add_user():
#     global glo_list
#     n = input('请输入您要注册的用户名: ')
#     p = input('请输入该用户密码: ')
#     dict01 = {}
#     dict01['name'] = n
#     dict01['password'] = p
#     glo_list.append(dict01)
#     main()
#
#
# def panduan():
#     global glo_list
#     n = input('请输入您要查询的用户名: ')
#     for i in glo_list:
#         if i['name'] == n:
#             print('该用户已存在')
#             main()
#     else:
#         print('该用户不存在')
#         main()
#
#
#
# if __name__ == '__main__':
#     main()



# from selenium import webdriver
#
#
#
# driver = webdriver.Chrome()
# driver.get('http://www.baidu.com')
# data = driver.find_element_by_id('id="hotsearch-content-wrapper"').get_attribute('innerHTML')
# print('---------',data)

#----------------递归判断是否有嵌套的json
#
# data = {"data":{"admin": {'a':1},"chapterTops":[],"coinCount":0,"collectIds":[17666,17675,12554,18965],"email":"","icon":"","id":17180,"nickname":"liangchao","password":"","publicName":"liangchao","token":"","type":0,"username":"liangchao"},"errorCode":0,"errorMsg":""}
#
# #有出口，当发现没有嵌套的json时就结束，传入的每一个key对应的value不是dict时
#
# def fun(**kwargs):
#     print(f'传入的数据为：{kwargs}')
#     for i in kwargs.keys():
#         print('kwargs[i]:',i,kwargs[i])
#         if isinstance(kwargs[i],dict):
#             print('有嵌套json')
#             fun(**kwargs[i])
#
#
#
#
# #自己调用自己
# fun(**data)


# dictory={"key1":"value1","key2":"value2"}
#
# if isinstance(dictory,dict):
#     print('dict')

# start = 5
# end = 6
#
# re = (start+end>>1)
# print(re)


# a = 1
# print(id(a))
# b = a
# print(id(b))
# a = a + 1
# print(id(a))
# c = 1
# print(id(c))

a = 1
b = a
c = 1
print(id(a))
print(id(b))
print(a == b)
print(a is b)
print(a is c)

a = 257
b = 257
print(id(a))
print(id(b))
print(a == b)
print(a is b)
print(a is c)

a = [1, 2, 3]
b = [1, 2, 3]
print(a, b)
print(a == b)
print(id(a), id(b))
print(a is b)