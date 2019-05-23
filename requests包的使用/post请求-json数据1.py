#coding:utf-8
__author__ = 'lc'




#1---导入
import requests,json


# 发送Post请求

urlstr = 'http://httpbin.org/post'

payload = {'qq群名':'selenium+jmeter+loadrunner','qq群号':'106014970'}

#通过json.dumps方法将Python字符串转换成json类型
payload = json.dumps(payload)

#2---发送请求
r  = requests.post(url=urlstr,data=payload)

#3---获取结果
print(r.text)

#返回为json类型，既可以通过r.json方法来查看结果
print(r.json())









