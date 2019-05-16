#coding:utf-8
# __author__ = 'lc'


f = open('E:\code\VIPtest2\data2.txt','r')


newData = f.readlines()

print(newData)

f.close()

def GetNum(*newData):
    for i in newData:
        print(i)

GetNum(*newData)