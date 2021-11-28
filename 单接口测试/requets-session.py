


import requests

#登陆接口
url1='https://www.wanandroid.com/user/login'
#查看收藏文章列表接口
url2 = 'https://www.wanandroid.com/lg/collect/list/0/json'

data={
    'username':'liangchao',
    'password':'123456'
}
# #请求登陆接口
# r1 = requests.post(url=url1,data=data)
# print(r1.content)
# #请求收藏的接口
# r2 = requests.get(url=url2)
# print(r2.text)

s = requests.Session() #自动携带token对象，有登录密码

r1 = s.post(url1,data=data)

r2 = s.get(url2) #用这个对象调用目标接口

# print(r2.json)