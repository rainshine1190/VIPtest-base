"""
需求：有一堆字符串，“welocme to super&Test”，打印出superTest，不能查字符的索引

分析：先用split分割字符串得到super&Test，然后再继续分割&

"""

str1 = 'welocme to super&Test'

str2 = str1.split(' ')[-1]
list1 = str2.split('&')
result = ''.join(list1)
print(result)