"""
功能描述：
编写人：liangchao
编写日期：
实现逻辑：
导包
    1-
    2-
    3-

"""
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
r1 = requests.post(url=url1,data=data)
print(r1.content)
print(dict(r1.cookies))
print(r1.cookies['JSESSIONID'])
c = r1.cookies['JSESSIONID']

header = {
    'Cookie':'JSESSIONID='+c
}
#
print(header)
# #请求收藏的接口
r2 = requests.get(url=url2,headers = header)
print(r2.text)