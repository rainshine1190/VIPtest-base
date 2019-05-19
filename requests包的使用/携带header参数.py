#coding:utf-8
__author__ = 'lc'



#1---导入
import requests


# 发送GET请求

urlstr = 'https://www.wanandroid.com/blog/show/2'

header = {'User-Agent':'Mozilla/6.0'}

cookie = {'Set-Cookie':'JSESSIONID=7FD4638D18876336AFDF8DA8C3DD8B95'}

#2---发送请求
s = requests.session()

r  = s.get(url=urlstr,headers=header,cookies=cookie)

#3---获取结果
# print(r.text)
print(r.headers)
print(r.cookies)








