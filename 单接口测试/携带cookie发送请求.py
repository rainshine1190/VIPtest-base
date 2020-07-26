

import requests

url = 'https://www.wanandroid.com/user/login'


p={'username':'liangchao','password':'123456'}

r=requests.post(url=url,data=p)

cookie = r.cookies

url2 = 'https://www.wanandroid.com/lg/todo/list/0'
re = requests.get(url2,cookies=cookie)
# re = requests.get(url2)

print(re.text)
