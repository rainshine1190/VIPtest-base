#coding:utf-8
__author__ = 'lc'


import requests


# 发送GET请求

urlstr = 'https://www.wanandroid.com/article/query'

#参数
param = {'k':'Android'}

#2---发送请求
r  = requests.get(url=urlstr,params=param)

#3---获取结果
print(r.text)
print(r.status_code)






