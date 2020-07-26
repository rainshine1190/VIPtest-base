
#导入包
import requests

url = 'http://www.baidu.com'


#请求
r = requests.get(url,headers={'agent':'chrome'})

#查看
print(r)
print(r.text)
print(r.content)
print(r.headers)



