#coding:utf-8
__author__ = 'lc'




#1---导入
import requests,json


# 发送Post请求

urlstr = 'http://httpbin.org/post'

payload = {'qq群名':'selenium+jmeter+loadrunner','qq群号':'106014970'}


#2---发送请求，接口请求为json数据，通过json=自动将Python对象转变为json类型
r  = requests.post(url=urlstr,json=payload)

#3---获取结果
print(r.text)

#返回为json类型，既可以通过r.json方法来查看结果
print(r.json())









