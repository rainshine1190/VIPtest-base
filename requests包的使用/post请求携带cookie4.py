#coding:utf-8
__author__ = 'lc'

'''
通过定制cookie，放入header来访问目标网址

'''
#1---导入
import requests,re


# 发送Post请求

urlstr = 'https://www.wanandroid.com/user/login'

data = {'username':'liangchao','password':'123456'}

#2---发送请求
r  = requests.post(url=urlstr,data=data)
print('***',r.text)
print('***',r.cookies)
print('***',r.headers)
print(r.cookies['JSESSIONID'])

#获取上次请求放回的response中的cookie，通过字典的形式引用cookie返回的JSESSIONID，放入下次请求header中

header = {
    'cookie':'JSESSIONID='+r.cookies['JSESSIONID']
}


#携带header发送请求

r2 = requests.get('https://www.wanandroid.com/lg/todo/list/0',headers = header)


print('****',r2.text)
print('****',r2.headers)

#str.find方法返回-1表示未找到，非-1表示找到
result = r2.text.find("已完成清单")
print(result)
if result != -1:
    print('查询成功')
else:
    print('查询失败')

#或通过正则来查找
pattern = re.compile(r';\">(.*?)<\/h2>')
result = pattern.findall(r2.text)
print(result)








