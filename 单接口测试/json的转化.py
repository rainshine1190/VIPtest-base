


import requests,json

#登陆接口
url1='https://www.wanandroid.com/user/login'
#查看收藏文章列表接口
url2 = 'https://www.wanandroid.com/lg/collect/list/0/json'

data={
    'username':'liangchao',
    'password':'123456'
}

#请求登陆接口
r1 = requests.post(url=url1,data=data)
print(r1.text)
print(type(r1.text))
re = json.loads(r1.text)
print(type(re))
print(re['data'])