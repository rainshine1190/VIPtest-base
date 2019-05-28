#coding:utf-8
__author__ = 'lc'

'''
通过rquests.session自动设置cookie，来完成访问
'''


#1---导入
import requests

# 发送Post请求

urlstr = 'https://www.wanandroid.com/user/login'

data = {'username':'liangchao','password':'123456'}


#初始化session对象
s = requests.session()

#2---通过session对象发送请求,# 服务器设置在本地的cookie会保存在本地
r  = s.post(url=urlstr,data=data)

#通过session继续发送post请求，自动携带上一个请求返回的cookie
r2 = s.get('https://www.wanandroid.com/lg/todo/list/0')


print('****',r2.text)
print('***',r.text)





#会带上之前保存在seesion中的cookie，能够请求成功
r2 = s.get('https://www.wanandroid.com/lg/todo/list/0')


print('***',r2.text,r2.status_code)

# #3---获取结果
# print(r.text)
# #查看类型
# print(type(r.json()))
# #通过dict-key来访问对应的值
# print(r.json()['data']['username'])
#
# print('***',r.cookies)
# token = dict(r.cookies)['token_pass']
# print(token)
# print('***',r.headers)
# cookie = type(r.headers['Set-Cookie'])
# cookie = r.headers['Set-Cookie'].split(';')[0]
# print(cookie)

#获取请求的header












