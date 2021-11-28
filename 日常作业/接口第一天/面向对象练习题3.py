#coding:utf-8


# 3、摆放家具
# 需求：
# 1）.房子有户型，总面积和家具名称列表
#    新房子没有任何的家具
# 2）.家具有名字和占地面积，其中
#    床：占4平米
#    衣柜：占2平面
#    餐桌：占1.5平米
# 3）.将以上三件家具添加到房子中
# 4）.打印房子时，要求输出:户型，总面积，剩余面积，家具名称列表

'''
1.需要定义的类：房子；家具
2.房子类的属性：户型、总面积、家具列表，剩余面积
2.1房子的方法：添加家具
    2.1.1添加家具方法的实现
        剩余面积减少（家具的占地面积）
        家具列表增加一个家具
3.家具的属性：名称；占地面积
3.1家具的方法：
'''








class House(object):

    def __init__(self,apartment,total_area):
        self.apartment = apartment
        self.total_area = total_area
        self.residue = self.total_area
        self.item_list = []
    def __str__(self):
        return "房子户型是：%s，总面积：%d平，剩余面积：%d平，家具有：%s" % (self.apartment,self.total_area,self.residue,self.item_list)

    def add_item(self,item):
        if item.cover_area > self.residue:
            print("%s的面积太大，屋里放不下" % (item.name))
        else:
            self.residue = self.residue - item.cover_area
            self.item_list.append(item.name)
            print("给房子添加家具：%s" % item.name)

class Furniture(object):
    def __init__(self,name,cover_area):
        self.name = name
        self.cover_area = cover_area

    def __str__(self):
        return "家具%s占地%0.1f平" % (self.name,self.cover_area)


h = House('三室两厅',200)
print(h)
f1 = Furniture('床',4)
f2 = Furniture('衣柜',2)
f3 = Furniture('餐桌',1.5)

print(f1)
print(f2)
print(f3)

h.add_item(f1)
print(h)
h.add_item(f2)
print(h)




