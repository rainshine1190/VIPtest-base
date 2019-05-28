#coding:utf-8
__author__ = 'lc'




import re

# print(re.match('www', 'www.runoob.com').span())  # 在起始位置匹配
#
#
# result = re.match('com', 'comwww.runoob.com')         # 不在起始位置匹配
# print(result)


#
# print(re.search('www', 'www.runoob.com').span())  # 在起始位置匹配
# print(re.search('com', 'www.runoob.com').span())         # 不在起始位置匹配
#
# result = re.search('www','www.baidu.com.www').span()
# print(result)
# # print(result.group(0))

pattern = re.compile(r'[a-z]')
result = pattern.findall('1ljslfjs2ndlsjflhell4o')
print(result)



