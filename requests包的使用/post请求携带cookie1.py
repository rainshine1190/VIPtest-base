#coding:utf-8
__author__ = 'lc'

'''
通过r.cookies手动获取上一请求返回的cookie来设置下次请求的cookie

'''
#1---导入
import requests


# 发送Post请求
urlstr = 'https://www.wanandroid.com/user/login'

data = {'username':'liangchao','password':'123456'}

#2---发送请求
r  = requests.post(url=urlstr,data=data)
print('***',r.text)
print('***',r.cookies)
print('***',r.headers)

#获取上次请求放回的response中的cookie，传递给下次请求
cookie = r.cookies

#携带cookie发送请求
r2 = requests.get('https://www.wanandroid.com/lg/todo/list/0',cookies = cookie)
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












