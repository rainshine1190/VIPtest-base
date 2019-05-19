#coding:utf-8
__author__ = 'lc'




#1---导入
import requests


# 发送Post请求

urlstr = 'https://www.wanandroid.com/user/login'

data = {'username':'liangchao','password':'123456'}

#2---发送请求
r  = requests.post(url=urlstr,data=data)

#3---获取结果
print(r.text)
#查看类型
print(type(r.json()))
#通过dict-key来访问对应的值
print(r.json()['data']['username'])







