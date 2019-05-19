#coding:utf-8
__author__ = 'lc'




#
# #打印返回结果
# print(r.text)
# print(type(r.text))
#
# print(r.content)
#
#
# print(r.raw)
# print(type(r.raw))
# #返回响应的json串
# print(r.json())
# #通过字典的key来获取json中的value
# print(r.json()['headers'])
# print(type(r.json()))


#3---header使用：

# headers = {'user-agent': 'Mozilla/5.0'}
#
# r  = requests.get(url=url,headers = headers)
# #查看返回的user-agent是否变化，可以通过改变header中的内容来模拟不同的请求来源
# print(r.text)
# print(r.request)



#4----get携带参数

# param = {'k':'hello'}
# r = requests.get(url='https://www.wanandroid.com/article/query',params=param)
# print(r.text)
# print(r.status_code)
# print(r.cookies)

#----post携带参数

# url = 'https://www.wanandroid.com/user/login'
# data = {'username':'liangchao','password':'123456'}
# r = requests.post(url = url,data=data)
# print(r.text)


# 要发送POST请求，只需要把get()方法变成post()，然后传入data参数作为POST请求的数据：
#
# >>> r = requests.post('https://accounts.douban.com/login', data={'form_email': 'abc@example.com', 'form_password': '123456'})
# requests默认使用application/x-www-form-urlencoded对POST数据编码。如果要传递JSON数据，可以直接传入json参数：
#
# params = {'key': 'value'}
# r = requests.post(url, json=params) # 内部自动序列化为JSON
# 类似的，上传文件需要更复杂的编码格式，但是requests把它简化成files参数：
#
# >>> upload_files = {'file': open('report.xls', 'rb')}
# >>> r = requests.post(url, files=upload_files)
# 在读取文件时，注意务必使用'rb'即二进制模式读取，这样获取的bytes长度才是文件的长度。
#
# 把post()方法替换为put()，delete()等，就可以以PUT或DELETE方式请求资源。



#cookie的获取
# url = 'https://wanandroid.com/wxarticle/list/408/1/json'
#
# r = requests.get(url)
# print(r.cookies['JSESSIONID'])

#携带cookie
# cookies={'JSESSIONID': '1234567890'}
# url = 'https://wanandroid.com/wxarticle/list/408/1/json'
#
# r = requests.get(url,cookies=cookies)
# # print(r.cookies['JSESSIONID'])
# # print(r.text)
# print(r.cookies)
# print(r.headers)

#设置超时

# r = requests.get(url, timeout=2.5)


