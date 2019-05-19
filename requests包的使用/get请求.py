#coding:utf-8
__author__ = 'lc'

#1---导入
import requests


# 发送GET请求

urlstr = 'https://www.wanandroid.com/blog/show/2'

#2---发送请求
r  = requests.get(url=urlstr)

#3---获取结果
print(r.text)
print(r.headers)












