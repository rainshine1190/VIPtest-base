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

list1 = ['1','2','3']
list2 = [3,4,5]

dict1 = {list1[i]:list2[i] for i in range(len(list2))}
print(dict1)




