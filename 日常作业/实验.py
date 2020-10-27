
list1=[1,2,3,4]
def add(*args):
    print(args)

add(*list1)
(1, 2, 3, 4)

dict1 = {'name': 'TOM', 'age': 18, 'id': 110}

{'name':'tom','age':18,'id':110}
#
# dict1 = {'a':1,'b':2,'c':3}
#
# #形式参数：形参
# def add(**kwargs):
#     print(kwargs)
# #实际参数：实参
# add(**dict1)


# list1 = [1,8,2,7,6,5]
# list1.sort()
# print(list1)


#
# import functools
# list1 = [1, 2, 3, 4, 5]
# def func(a, b):
#     return a + b
# result = functools.reduce(func, list1)
# print(result)
#
#
#
# file = open('data.txt','r')
#
#
# file.close()
#
#
# with open() as f:
#     f.read()


'''
lucy:21，tom:30
'''

# str1 = 'lucy:21,tom:30'
#
# list1 = str1.split(',')
# print(list1)
# dict1 = {}
# for
#     for i in list1:
#         key = i.split(':')[0]
#         value = i.split(':')[1]
#         print(key,value)
#         dict1[key] = value
#
#
# print(dict1)


# dict1 = {'lucy': '21', 'tom': '30'}
# if 'luc' in dict1:
#     print('in')
# else:
#     print('not in')


# def func():
#     a = input()
#     b = input()
#     c = a+b
#     print(c)
#
# func()



#外层循环变量初始值
i = 1
list0 = []
#循环体
while i < 3:
    #先写内层循环
    j = 0
    #循环体
    while j < 3:
        list0.append((i,j))
        j = j + 1
    #外层循环变量发生变化
    i = i + i

print(list0)