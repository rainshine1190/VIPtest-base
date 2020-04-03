# def fun(x):
#     x = x**2
#     return x
#
# print(fun(3))

# result = lambda x:x**2
# print(result(3))

import os

dir = os.path.dirname(os.path.abspath(__file__))
re = lambda fn: os.path.getatime(dir + "\\" + fn) if not os.path.isdir(dir +"\\"+ fn)else 0


print(re('__init__.py'))



list1.sort(key='a')