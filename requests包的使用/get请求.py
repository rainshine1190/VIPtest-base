#coding:utf-8
__author__ = 'lc'

#1---导入
import requests


# 发送GET请求

urlstr = 'https://blog.csdn.net/rainshine1190'

#2---发送请求
r  = requests.get(url=urlstr,timeout=5)

print(r.text)


print(r.content)
r.encoding = 'gbk'
print(r.encoding)
#3---获取结果
print(r.text)
#查看响应头
print(r.headers)












