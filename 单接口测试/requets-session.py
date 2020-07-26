


import requests

url='https://www.wanandroid.com/user/login'
data={
    'username':'jzw',
    'password':'w616616'
}


s = requests.session() #自动携带token对象，有登录密码
r = s.post(url,data=data)

url1 = 'https://www.wanandroid.com/lg/todo/list/0'

resp2 = r.get(url1) #用这个对象调用目标接口

print(resp2.text)