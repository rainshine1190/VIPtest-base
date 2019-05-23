#coding:utf-8
# __author__ = 'lc'

#
# try:
#     a = int(input('please input the num:'))
#
#     if a > 0:
#         a += 10
#     elif a == 0:
#         a += 20
#     else:
#         a += 30
#     print(a)
#
#
# except ValueError:
#     print('请输入数字！')



# print(range(1,10))

#
# def sum(a,b):
#     return a + b

# def sum(b=1,a):
#     return a + b
#
#
#
# sum(1,2)
# def add_end(L=[]):
#     L.append('END')
#     return L
#
# print(add_end())
# print(add_end())


# def add_end(L=None):
#     if L is None:
#         L = []
#     L.append('END')
#     return L
#
# print(add_end())
# print(add_end())



# def calc(*numbers):
#     print(*numbers)
#     print(numbers)
#     sum = 0
#     for n in numbers:
#         sum += n
#     return sum
#
# num = [1,2,3]
# print(calc(*num))




# def person(name,age,**kwargs):
#     print('name',name,'age',age,kwargs)
#
#
# extra = {'city': 'Beijing', 'job': 'Engineer'}
# person('xiaoming',25,**extra)



# def product(x, *num):
#     for i in num:
#         x = x * i
#     return x
#
# print(product(1))

# a = int(input('please input：'))
#
# s = 1
# while a>0:
#     s = s*a
#     a -= 1
#
# print(s)

# def mul(n):
#     if n == 1:
#         return 1
#     if n>0:
#         return n * mul(n-1)
#
# print(mul(5))

#
# def fbnq(n):
#     print(a)
#     c = a + b
#     a = b
#     b = c

#
# import requests
# help(requests.session())



# import json
# help(json)



# coding:utf-8
import requests
body = {"key1": "value1",
        "key2": "value2"}  # 这里账号密码就是抓包的数据

s = requests.session()
login_url = "http://xxx.login"   #　自己找带token网址

login_ret = s.post(login_url, data=body)

# 这里token在返回的json里，可以直接提取
token = login_ret.json()["token"]

# 这是登录后发的一个post请求
post_url = "http://xxx"
header = {}
# 添加token到请求头
header["token"] = token
# 如果这个post请求的头部其它参数变了，也可以直接更新
header["Content-Length"]="9"
body1 = {
         "key": "value"
         }
post_ret = s.post(post_url, headers=header, data=body1)
print(post_ret.content)
