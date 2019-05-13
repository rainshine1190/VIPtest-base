#coding:utf-8
# __author__ = 'lc'




#------------------------------读取--------------
#打开文件open，两个常用参数：文件路径和打开模式
#路径支持绝对和相对路径；
# 模式：r：读；r+：读写  w：写（覆盖/新建）  w+：读写（覆盖/新建） a：追加（存在的时候追加；没有的时候新建）

f = open('E:\code\VIPtest2\data2.txt','r')

#读取文件全部内容，或读取制定长度字节的数据
# print(f.read())
# print(f.read(4))

#读取整行
# print(f.readline())

#读取所有行，作为一个列表输出
print(f.readlines())


f.close()









