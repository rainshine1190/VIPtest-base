# # """
# #
# # 1、打印小猫爱吃鱼，小猫要喝水
# # 2、小明爱跑步，爱吃东西。
# # 1）小明体重75.0公斤
# # 2）每次跑步会减肥0.5公斤
# # 3）每次吃东西体重会增加1公斤
# # 4）小美的体重是45.0公斤
# #
# #
# #
# # """
# #
# #
# # """
# # 1-类：Cat
# # 属性：
# # 方法：eat_fish drink_water
# #
# # """
# #
# # # class Cat(object):
# # #
# # #     def eat_fish(self):
# # #         print('小猫爱吃鱼')
# # #
# # #     def drink_water(self):
# # #         print('小猫要喝水')
# # #
# # #
# # # tom = Cat()
# # # tom.eat_fish()
# # # tom.drink_water()
# #
# #
# # #分析：
# #
# # '''
# # 类：Person
# # 属性：name，weight
# #
# # 方法：run，eat
# # run：weight - xx斤
# #
# #
# #
# #
# #
# # '''
# #
# # # class Person(object):
# # #
# # #     def __init__(self,name,weight):
# # #         self.name = name
# # #         self.weight = weight
# # #
# # #     def run(self):
# # #         self.weight -= 0.5
# # #         print(f'{self.name}跑步，体重减少了，现在重{self.weight}公斤')
# # #
# # #     def eat(self):
# # #         self.weight += 1
# # #         print(f'{self.name}吃东西，体重增加了，现在重{self.weight}公斤')
# # #
# # #     def __str__(self):
# # #         return f'{self.name}体重是{self.weight}公斤'
# # #
# # #
# # #
# # # p = Person('xm',75.0)
# # # print(p.weight)
# # # print(p)
# # # p.run()
# # # print(p.weight)
# # #
# # #
# # #
# # # m = Person('xh',50.0)
# # # m.eat()
# # #
# # #
# #
# #
# # """
# # 3、摆放家具
# # 需求：
# # 1）.房子有户型，总面积和家具名称列表
# #    新房子没有任何的家具
# # 2）.家具有名字和占地面积，其中
# #    床：占4平米
# #    衣柜：占2平面
# #    餐桌：占1.5平米
# # 3）.将以上三件家具添加到房子中
# # 4）.打印房子时，要求输出:户型，总面积，剩余面积，家具名称列表
# #
# #
# # """
# #
# #
# # '''
# # 类：家/房子
# # 属性：户型、面积、（剩余面积）、家具列表
# # 方法：
# #     初始化
# #     添加家具
# #     __str__
# #
# # 类：家具
# # 属性：名字、占地面积
# # 方法：
# #
# # '''
# # #
# # # class Furnicure(object):
# # #
# # #     def __init__(self,name,cover_area):
# # #         self.name = name
# # #         self.cover_area = cover_area
# # #
# # #
# # # class Home(object):
# # #
# # #     def __init__(self, hx, area):
# # #
# # #         self.hx = hx
# # #         self.area = area
# # #         self.jiaju_list = []
# # #         self.symj = self.area
# # #
# # #     def add_jiaju(self,item):
# # #         """往房子里添加家具，房子的面积就减少了"""
# # #         if self.symj >= item.cover_area:
# # #             self.symj = self.area - item.cover_area
# # #             print(f'房子添加完家具{item.name}后，剩余面积是{self.symj}')
# # #         else:
# # #             print('房子太小了，放不下了')
# # #
# # #
# # #
# # # bed = Furnicure('床',200)
# # # print(bed.name,bed.cover_area)
# # #
# # # house = Home('三室一厅', 120)
# # # print(house.hx,house.area)
# # #
# # # house.add_jiaju(bed)
# #
# #
# #
# #
# # """
# # 烤地瓜
# #
# #
# #
# # """
# # # # #定义一个类.地瓜
# # # class Potato(object):
# # #     #定义构造函数.初始化属性.  时间0,状态生的,不加调料
# # #     def __init__(self):
# # #         self.status = "生的"
# # #         self.time = 0
# # #         self.cooper = []
# # #
# # #     #定义cook烤地瓜方法.
# # #     def cook(self, time,cooper=''):
# # #         #
# # #         self.cooper.append(cooper)
# # #         self.time = self.time + time
# # #         if 0 <= self.time < 3:
# # #             self.status = "生的"
# # #         elif 3 <= self.time < 5:
# # #             self.status = "半生不熟"
# # #         elif 5 <= self.time < 8:
# # #             self.status = "熟的"
# # #         else:
# # #             self.status = "烤糊了"
# # #
# # #
# # #
# # #     def __str__(self):
# # #         #定义类的解释
# # #         return "这个地瓜考了{0}分钟,状态是{1},调料：{2}".format(self.time, self.status, self.cooper)
# # #
# # #
# # # p = Potato()
# # # print(p)
# # #
# # # p.cook(2,'孜然')
# # # print(p)
# # # p.cook(2,'辣椒')
# # # print(p)
# #
# #
# # # title = ["id","interfaceUrl","name","Method","value","expect","real","status"]
# # # case = ['1', 'https://www.wanandroid.com/user/login', 'login', 'post', "{'username':'liangchao','password':'123456'}", '0', '', '']
# # #
# # # dict1 = {title[i]:case[i] for i in range(len(title))}
# # # print(dict1)
# #
# # # import xlrd
# # #
# # # excel = xlrd.open_workbook()
# # # sheet = excel.sheet_by_index()
# # # excel.sheet_by_name()
# # #
# # # sheet.nrows
# # # sheet.ncols
# # #
# # # sheet.row_values()
# # # sheet.col_values()
# # #
# # #
# # # sheet.cell_value()
# #
# # # list1 = ['1','2','3']
# # # list2 = [3,4,5]
# # #
# # # dict1 = {list1[i]:list2[i] for i in range(len(list2))}
# # # print(dict1)
# # #
# #
# #
# #
# # # def num1 (a,b):
# # #     sum = input("输入的数组：")
# # #     for i in sum:
# # #         a = b+a
# # #         b = a
# # #         a = b
# # #         i +=1
# # #         return
# # # num1(5)
# #
# # #
# # # lis1 = [1,2,3,4,5,5,2,3,2,4]
# # #
# # # for i in lis1:
# # #     lis1.count(i)
# # #     lis1.pop(i)
# # #     lis1.sort()
# # # print(lis1)
# # # 运行结果为：
# # # [1, 2, 3, 4, 5]
# #
# #
# #
# # # str ="welocme to super&Test"
# # # i = str.split(' ')
# # # str_list = []
# # # while(i >= 0):
# # #     str_list.append(str[i])
# # #     i = i - 1
# # # print(''.join(str_list))
# #
# #
# # # a =1
# # # b =1
# # # for i in range(10):
# # #     a ,b = b ,(a+b)
# # #     print(a)
# #
# #
# #
# # # glo_list=[]
# # #
# # # def main():
# # #     print('----------------------------')
# # #     print('---1-注册；2-查询；3-退出------')
# # #     print('----------------------------')
# # #     a = int(input('请选择您要的功能：'))
# # #     if a == 1:
# # #         add_user()
# # #     elif a == 2:
# # #         panduan()
# # #     elif a == 3:
# # #         print('退出系统')
# # #         exit()
# # #     else:
# # #         print('请输入合法字符！')
# # #
# # #
# # #
# # # def add_user():
# # #     global glo_list
# # #     n = input('请输入您要注册的用户名: ')
# # #     p = input('请输入该用户密码: ')
# # #     dict01 = {}
# # #     dict01['name'] = n
# # #     dict01['password'] = p
# # #     glo_list.append(dict01)
# # #     main()
# # #
# # #
# # # def panduan():
# # #     global glo_list
# # #     n = input('请输入您要查询的用户名: ')
# # #     for i in glo_list:
# # #         if i['name'] == n:
# # #             print('该用户已存在')
# # #             main()
# # #     else:
# # #         print('该用户不存在')
# # #         main()
# # #
# # #
# # #
# # # if __name__ == '__main__':
# # #     main()
# #
# #
# #
# # # from selenium import webdriver
# # #
# # #
# # #
# # # driver = webdriver.Chrome()
# # # driver.get('http://www.baidu.com')
# # # data = driver.find_element_by_id('id="hotsearch-content-wrapper"').get_attribute('innerHTML')
# # # print('---------',data)
# #
# # #----------------递归判断是否有嵌套的json
# # #
# # # data = {"data":{"admin": {'a':1},"chapterTops":[],"coinCount":0,"collectIds":[17666,17675,12554,18965],"email":"","icon":"","id":17180,"nickname":"liangchao","password":"","publicName":"liangchao","token":"","type":0,"username":"liangchao"},"errorCode":0,"errorMsg":""}
# # #
# # # #有出口，当发现没有嵌套的json时就结束，传入的每一个key对应的value不是dict时
# # #
# # # def fun(**kwargs):
# # #     print(f'传入的数据为：{kwargs}')
# # #     for i in kwargs.keys():
# # #         print('kwargs[i]:',i,kwargs[i])
# # #         if isinstance(kwargs[i],dict):
# # #             print('有嵌套json')
# # #             fun(**kwargs[i])
# # #
# # #
# # #
# # #
# # # #自己调用自己
# # # fun(**data)
# #
# #
# # # dictory={"key1":"value1","key2":"value2"}
# # #
# # # if isinstance(dictory,dict):
# # #     print('dict')
# #
# # # start = 5
# # # end = 6
# # #
# # # re = (start+end>>1)
# # # print(re)
# #
# #
# # # a = 1
# # # print(id(a))
# # # b = a
# # # print(id(b))
# # # a = a + 1
# # # print(id(a))
# # # c = 1
# # # print(id(c))
# #
# # # a = 1
# # # b = a
# # # c = 1
# # # print(id(a))
# # # print(id(b))
# # # print(a == b)
# # # print(a is b)
# # # print(a is c)
# # #
# # # a = 257
# # # b = 257
# # # print(id(a))
# # # print(id(b))
# # # print(a == b)
# # # print(a is b)
# # # print(a is c)
# # #
# # # a = [1, 2, 3]
# # # b = [1, 2, 3]
# # # print(a, b)
# # # print(a == b)
# # # print(id(a), id(b))
# # # print(a is b)
# #
# #
# # class Stack(object):
# #     def __init__(self):
# #         self.items = []
# #
# #     def is_empty(self):
# #         """判断是否为空集"""
# #         return self.items == []
# #
# #     def push(self, item):
# #         """添加新元素到栈顶"""
# #         self.items.append(item)
# #
# #     def pop(self):
# #         """删除栈顶元素"""
# #         return self.items.pop()
# #
# #     def peek(self):
# #         """窥探栈顶元素"""
# #         return self.items[-1]
# #
# #     def size(self):
# #         """查看栈的大小"""
# #         return len(self.items)
# #
# # if __name__ == '__main__':
# #     stack = Stack()
# #     print(stack.is_empty())
# #     stack.push(2)  # 入栈
# #     stack.push(3)  # 入栈
# #     print(stack.size())
# #     print(stack.peek())
# #     stack.pop()  # 出栈
# #     print(stack.size())
# #
# #
#
#
# # #2、跟踪非局部变量值  PySnooper 是以函数为单位进行调试的，它默认只会跟踪函数体内的局部变量，
# # # 若想跟踪全局变量，可以给 pysnooper.snoop() 加上 watch 参数
# # import pysnooper
# #
# # out = {"foo": "bar"}
# # @pysnooper.snoop(watch='out["foo"]')
# # def demo_func():
# #     dict_list = dict()
# #     dict_list["name"] = "dyf"
# #     dict_list["age"] = 18
# #     dict_list["gender"] = "female"
# #     return dict_list
# # demo_func()
# #
# # #和 watch 相对的，pysnooper.snoop() 还可以接收一个函数 watch_explode，
# # # 表示除了这几个参数外的其他所有全局变量都监控。
# # @pysnooper.snoop(watch_explode=('foo', 'bar'))
# # def demo_func():
# #     dict_list = dict()
# #     dict_list["name"] = "dyf"
# #     dict_list["age"] = 18
# #     dict_list["gender"] = "female"
# #     return dict_list
# # demo_func()
#
# import abc
#
#
# # 创建抽象类
# class Animal(metaclass=abc.ABCMeta):
#     # 移动接口
#     @abc.abstractmethod
#     def move(self):
#         pass
#
#     # 进食接口
#     @abc.abstractmethod
#     def eat(self):
#         pass
#
#
# # 定义人类
# class Human(Animal):
#     # 移动接口
#     def move(self):
#         print("Human is walking")
#
#     # 进食接口
#     def eat(self):
#         print("Human is eating")
#
#
# # 定义狗类
# class Dog(Animal):
#     # 移动接口
#     def move(self):
#         print("Dog is running")
#
#     # 进食接口
#     def eat(self):
#         print("Dog is eating")
#
#
# # 定义猫类
# class Cat(Animal):
#
#     def move(self):
#         print('paole')
#
#     # 移动接口
#     def run(self):
#         print("Dog is running")
#
#     # 进食接口
#     def eat(self):
#         print("Dog is eating")
#
#
#
# if __name__ == '__main__':
#     # 实例化得到一个人和一条狗
#     h1 = Human()
#     d1 = Dog()
#     c1 = Cat()  # TypeError: Can't instantiate abstract class Cat with abstract method move
#     # 调用移动接口
#     h1.move()
#     d1.move()
#     c1.move()


# import re
#
# str1 = "2018-05-31"
#
# # search通过传入的第一个参数：正则表达式 来匹配 第二个参数：待匹配字符
# result = re.search(r'^(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})$', str1)
# print("匹配后的结果对象为: ", result)
# #
# print("group()获取表达式匹配到的整体结果:", result.group())
# print("group(1)获取第一组正则匹配到的结果", result.group('year'))
# print("group(2)获取第二组正则匹配到的结果", result.group('month'))
# print("group(3)获取第二组正则匹配到的结果", result.group('day'))
# print("groups()获取一个包含所有小组字符串的元组：", result.groups())


# import re
#
# # 将正则表达式编译成 Pattern 对象
# pattern1 = re.compile(r'\d+')
# # 将正则表达式编译成 Pattern 对象，区分大小写
# pattern2 = re.compile(r'\w+', re.I)
# print(pattern1)

#
# class Solution(object):
#     def twoSum(self, nums, target):
"""
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
# list1 = []
# for i in nums:
#     for j in nums[1:]:
#         if i + j == target:
#             list1.append(i)
#             list1.append(j)
#
# return list1
# --------------------------------------------

# c-i 的值在列表中，得到i和c-i的坐标
# list1 = []
# for i,j in enumerate(nums):
# print(i,j)
#             if target - j  in nums:
#                 list1.append(nums.index(j))
#                 list1.append(nums.index(target-j))
#                 break
#
#         return list1
# nums = [2,7,11,15]
#
# print(Solution().twoSum(nums, 9))

# class Solution(object):
#     def lengthOfLongestSubstring(self, s):
#         """
#         :type s: str
#         :rtype: int
#         思路：
#         1-遍历字符串到新的列表内，如果in为true则终止，max接受新列表的长度
#         且从i的索引处重新遍历
#         """
#         # s1 = list(s)
#         # s2 = []
#         # max = 0
#         # for i in s1:
#         #     if i not in s2:
#         #         s2.append(i)
#         #         if len(s2) > max:
#         #             max = len(s2)
#         #     else:
#         #         s2.clear()
#         #         s1 = s1[s1.index(i):]
#         #
#         # return len(s2)
#
#
#         # ---------------------------------------
#         s1 = list(s)
#         s2 = []
#         max = 0
#         for i,j in enumerate(s1):
#             if j not in s2:
#                 s2.append(j)
#                 if len(s2)>max:
#                     max = len(s2)
#             else:
#                 s2 = []
#                 s1 = s1[s1.index(j):]
#                 i = 0
#         return max
#
#
# print(Solution().lengthOfLongestSubstring("aab"))
#

"""
abcabcab

分析：
提前定义一个空列表
max = 0
1-遍历目标字符串，
    1.1-if该元素在列表中不存在
        则append
        if 新列表的长度大于max则将max重新赋值
        

"""
# class Solution(object):
#     def lengthOfLongestSubstring(self, s):
#         """
#         :type s: str
#         :rtype: int
#         思路：
#         1-遍历字符串到新的列表内，如果in为true则终止，max接受新列表的长度
#         且从i的索引处重新遍历
#         """
#         s1 = list(s)
#         s2 = []
#         max = 0
#         for m,n in enumerate(s1):
#             for i,j in enumerate(s1[m:]):
#                 if j not in s2:
#                     s2.append(j)
#                     if len(s2)>max:
#                         max = len(s2)
#                 else:
#                     s2 = []
#                     break
#         return max
#
#
# print(Solution().lengthOfLongestSubstring("abcabcb"))


# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         k, res, c_dict = -1, 0, {}
#         for i, c in enumerate(s):
#             if c in c_dict and c_dict[c] > k:  # 字符c在字典中 且 上次出现的下标大于当前长度的起始下标
#                 k = c_dict[c]
#                 c_dict[c] = i
#             else:
#                 c_dict[c] = i
#                 res = max(res, i-k)
#         return res

# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#
#         length = 0
#         queue = []
#
#         for i in s:
#             if i in queue:
#                 length = max(length, len(queue))
#                 # queue.pop(0)
#                 while i in queue:
#                     queue.pop(0)
#             else:
#
#                 queue.append(i)
#
#         return max(length, len(queue))
#
# print(Solution().lengthOfLongestSubstring("aab"))

# class Solution(object):
#     def lengthOfLongestSubstring(self, s):
#         """
#         :type s: str
#         :rtype: int
#         思路：
#
#         """
#         length = 0
#
#         queue = []
#         for i in s:
#             if i in queue:
#                 length = max(length,len(queue))
#                 if i in queue:
#                     queue.remove(queue[0])
#                     queue.append(i)
#             else:
#                 queue.append(i)
#         return max(length, len(queue))
#
# print(Solution().lengthOfLongestSubstring("pwwkew"))

#
# class Solution(object):
#     def lengthOfLongestSubstring(self, s):
#         """
#         :type s: str
#         :rtype: int
#         思路：
#
#         """
#         length = 0
#
#         queue = []
#         for i in s:
#             if i in queue:
#                 length = max(length,len(queue))
#                 if i in queue:
#                     queue.remove(queue[0])
#                 queue.append(i)
#
#         return max(length, len(queue))
#
# print(Solution().lengthOfLongestSubstring("abcabcab"))
#
# class Solution(object):
#     def lengthOfLongestSubstring(self, s):
#         se = set()
#         l = r = 0
#         length = max = 0
#
#         while r < len(s):
#             if s[r] not in se:
#                 se.add(s[r])
#                 r += 1
#                 length += 1
#                 max = length if length> max else max
#
#
#             else:
#                 while s[r] in se:
#                     se.remove(s[l])
#                     l += 1
#                     length -= 1
#                 se.add(s[r])
#                 length += 1
#                 r += 1
#
#         return max
#
# print(Solution().lengthOfLongestSubstring("abcabcab"))


# class Solution:
#     def addTwoNumbers(self, l1, l2):
#         flag = 0
#         l1.reverse()
#         l2.reverse()
#         l3 = []
#         length = max(len(l1), len(l2))
#         for i in range(length):
#             a = 0 if i >= len(l1) else l1[i]
#             b = 0 if i >= len(l2) else l2[i]
#             sum = a + b
#             sum = sum + flag
#             if sum >= 10:
#                 flag = 1
#             else:
#                 flag = 0
#             l3.append(sum % 10)
#         if flag:
#             l3.append(flag)
#         return l3
#
# l1 = [3,4,2]
# l2 = [4,6,5]
# print(Solution().addTwoNumbers(l1, l2))

#
# from array import *
#
# array1 = array('i', [10,20,30,40,20,50])
#
# print (array1.index(20))

# 编写一个函数来查找字符串数组中的最长公共前缀。如果不存在公共前缀，返回空字符串 ""。例如输入：strs = ["flower","flow","flight"] ，输出："fl"

"""
分析：
    1-判断一个字符是否在指定索引处
    2-取列表中最长长度的元素遍历
        遍历该元素时如果发现有一个元素不包含此字符则break，保存该索引
    3-返回该元素+索引的值

"""

# def inOrNot(str1,item,index1):
#     if item[index1] == str1:
#         return True
#     else:
#         return False
#
# def main():
#     maxL = 0
#     strs = ["flower", "flow", "flight"]
#     for i in strs:
#         for m,n in enumerate(i):
#             if inOrNot(n,i,m) and inOrNot(n,i):
#                 print(n,i,m)
#                 if m>=maxL:
#                     maxL = m
#             else:
#                 break
#     print(maxL)
#
# if __name__ == '__main__':
#     main()

# list1 = [1,3,8,2,4,5,7]
#
# for i in range(len(list1)):
#     for j in range(len(list1)-1-i):
#         if list1[j+1]>list1[j]:
#             list1[j+1],list1[j] = list1[j],list1[j+1]
#
# print(list1)

# # 二分查找
# list1 = [1, 2, 3, 4, 5, 6, 7, 8]
#
#
# def test(num, *args):
#     left, right = 0, len(args) - 1
#     while left <= right:
#         mid = (left + right) // 2
#         if num == args[mid]:
#             return mid
#         elif num < args[mid]:
#             right = mid - 1
#         else:
#             left = mid + 1
#     return -1
#
#
# print(test(8, *list1))


# # 二分查找
# list1 = [1, 2, 3, 4, 5, 6, 7, 8]
#
#
# def test(num,left,right,*args):
#     if num in args:
#         mid = (left+right)//2
#         if num == args[mid]:
#             return mid
#         elif num > args[mid]:
#             left = mid +1
#             return test(num,left,right,*args)
#         else:
#             right = mid -1
#             return test(num, left, right, *args)
#     else:
#         return -1
#
#
# print(test(8,0,7, *list1))


#
# def bubble_sort(arr):
#     n = len(arr)
#     # 控制已排序元素的个数
#     for i in range(n):
#         # 遍历未排序的元素，进行比较和交换
#         for j in range(0, n-i):
#             if j == n-i:
#                 break
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#     return arr
#
# list1 = [1,9,2,8,7,6,3,4]
# print(bubble_sort(list1))
#
# list1 = ["liower","fliow","flight1"]
#
# def findGong(arr):
#     maxlen = arr[0]
#     for i in arr:
#         if len(i)>len(maxlen):
#             maxlen = i
#     goal = ''
#     for m,n in enumerate(maxlen):
#         for i in arr:
#             if n in i:
#                 if n != i[m]:
#                     break
#             else:
#                 break
#         else:
#             goal += n
#     return goal
#
#
# print(findGong(list1))


# def longestCommonPrefix( strs:[str]) -> str:
#     if not strs:
#         return ""
#     for i in range(len(strs[0])):
#         for j in range(1, len(strs)):
#             if i >= len(strs[j]) or strs[j][i] != strs[0][i]:
#                 return strs[0][:i]
#     return strs[0]
#
# strs = ["flower","flow","flight"]
# print(main(strs))
#
# def main(strs):
#     if not strs:
#         return ''
#     for i in range(strs[0]):
#         for j in range(1,len(strs)):
#             if i >= len(strs[j]) or strs[j][i] != strs[j][i]:
#                 return strs[0][j]

"""

1,1,2,3,5,8

1,2,3,4,5,6,7,8,9,……100

100的累加和=100+99的累加和
99的累加和=99+98的累计和
98的累加和=98+97的累加和
……
2的累加和=2+1的累加和
1的累加和=1

"""

# =============================
# 1.递归实现斐波那契数列
# def fun1(n):
#     if n == 0:
#         return 1
#     if n == 1:
#         return 1
#     else:
#         return fun1(n - 1) + fun1(n - 2)
#
#
# list1 = []

# for i in range(20):
#     list1.append(fun1(i))
# print(list1)
#
#
# # 2.递归实现100累加和
# def fun2(sum):
#     if sum == 1:
#         return 1
#     return sum + fun2(sum - 1)
#
# print(fun2(100))


#
# # 3
#
#
# l1 = [9, 9, 9]
# sum = 0
# n = len(l1) - 1
# for i in l1:
#     sum = sum + (10 ** n) * i
#     n = n - 1
# sum = sum + 1
# str1 = str(sum)
# l1.clear()
# for i in str1:
#     l1.append(i)
#
# print(l1)



"""
给定一个由 整数 组成的 非空 数组所表示的非负整数，在该数的基础上加一。
最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。
你可以假设除了整数 0 之外，这个整数不会以零开头。

示例 1：

输入：digits = [1,2,3]
输出：[1,2,4]
解释：输入数组表示数字 123。

示例 2：
输入：digits = [4,3,2,1]
输出：[4,3,2,2]
解释：输入数组表示数字 4321。

示例 3：
输入：digits = [0]
输出：[1]

示例4：
输入：digits =[9]
输出：[1,0]

示例5：
输入：digits=[9,9,9]
输出：[1,0,0,0]

提示：

1 <= digits.length <= 100
0 <= digits[i] <= 9

"""

# import functools
#
# list1 = [1,2,3]
# list1 = map(str(),list1)
#
# cash = int(input("请输入您的消费金额："))
# if 2000>cash>=1000:
#     print(f'您优惠后的金额是：{cash*0.95}')
# elif 3000>cash>=2000:
#     print(f'您优惠后的金额是：{cash*0.9}')
# elif 5000>cash>=3000:
#     print(f'您优惠后的金额是：{cash*0.85}')
# elif cash>=5000:
#     print(f'您优惠后的金额是：{cash*0.8}')


"""
其思路是先统计每个字符在字符串中出现的次数，然后计算可以构成回文串的字符数量，
最后根据奇偶性判断是否还需要添加一个单独的字符作为中心点。如果字符的出现次数是偶数，
则可以作为加进回文串的长度，如果字符的出现次数是奇数，则在其数量上减1加进回文串的长度，
最后判断是否出现过奇数，如果出现过则可以放在回文串的中信位置，在回文串的长度加1。

"""

# def findNum(s):
#     #定义一个字典，保存每个字符出现的次数
#     dict1 = {}
#
#     for i in s:
#         dict1[i] = s.count(i)
#     #判断字典的每个value是奇数还是偶数
#     strLen = flag = 0
#     for j in dict1.values():
#         #如果是偶数，则累加进回文串长度中
#         if j % 2 == 0:
#             strLen += j
#         # 否则该数-1后，类加进回文串长度中，标记奇数是否出现过
#         else:
#             strLen += j-1
#             flag = 1
#     #循环结束后，判断奇数标记是否为True，则+1
#     if flag:
#         strLen += 1
#
#     return strLen
#
# print(findNum('aaaaaccc'))

# import numpy as np
# # 创建一个二维数组
# arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]])

# 访问数组中的元素
# print(arr[0, 0])  # 输出1
# print(arr[1, 2])  # 输出8

# 切片
# print(arr[0:1, 0:2])  # 输出[[1 2]]
# print(arr[0:2, 0:1])  # 输出[[1] [6]]
# print(arr[0:1, 0:2])  # 输出[[1] [6]]
# print(arr[0:2, 0:2])  # 输出[[1 2] [6 7]]

#
# X = np.array([[0,1,2,3],[10,11,12,13],[20,21,22,23],[30,31,32,33]])
#
# print(X[0:1,0:2])
# print(X[0:2,0:1])

#
def findNum(list1,target):

    left = 0
    right = len(list1)-1
    while left <= right:
        mid = (left + right) // 2
        if target > list1[mid]:
            left = mid + 1
        elif target < list1[mid]:
            right = mid -1
        else:
            return mid
    else:
        return -1

arr = list(range(1,100))
print(findNum(arr, 50))
