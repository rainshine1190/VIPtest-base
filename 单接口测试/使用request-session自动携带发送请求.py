

import requests


# help(requests.sessions)

url = 'http://www.wanandroid.com/lg/todo/add/json'
payload = {
    'title':'test3',
    'content':'我要吃饭',
    'date':'2020-07-25',
    'type':'0'
}

s = requests.session()
r = s.post(url=url,data=payload)
print(r.content)
