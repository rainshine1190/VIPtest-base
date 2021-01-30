

#导包
import os


#方法
#返回相对路径
# print(os.path.abspath(__file__))
# cur = os.path.abspath(__file__)
# #文件名
# print(os.path.basename(__file__))
# #文件的路径
# print(os.path.dirname(__file__))
#
# print(os.path.exists('D:/code/VIPtest3'))
#
# fileName = os.path.basename(__file__)
# fileDir = os.path.dirname(__file__)
# path = os.path.join(fileDir,fileName)
# print(path)
#
cur = os.path.abspath(__file__)
print('cur--',cur)
a1 = os.path.split(cur)

# a2 = list(a1)
# a2.append(3)
print(a1[-1])
