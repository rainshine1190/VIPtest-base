#coding:utf-8
__author__ = 'lc'



#1---导入
import requests


# 发送GET请求

urlstr = 'https://www.wanandroid.com/user/login'

header = {'User-Agent':'Mozilla/6.0'}

payload = {'username':'chaoge','password':'123456'}

#2---发送请求


r  = requests.post(url=urlstr,data= payload,headers=header)

#3---获取结果
print(r.text)
print(r.headers)








