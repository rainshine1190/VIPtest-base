
import requests


url = 'https://www.wanandroid.com/user/login'

p={'username':'fyq','password':'yz717826'}

r=requests.post(url=url,data=p)

print(r.text)

print(r.json())
dict2 = r.json()
print(dict2['errorCode'])