# str1 = 'hello'
# for i in str1:
#     if i == 'e':
#         print('遇到e不不打印')
#         continue
#     print(i)
# else:
#     print('循环正常结束之后执⾏行行的代码')


# a=int(input('斐波那契数列第几项？'))
#
# def num(b):
#     if b<=1:
#         return b
#     else:
#         return (num(b-2)+num(b-1))
#
#
# # print(num(a))
#
# for i in range(a):
#     print(num(i))

# import os.path
# import re
# import requests
# x=1
# s="https://www.ydniu.com/open/ssq-500.html"
# path=os.path.dirname(__file__)+r"/test.text"
# d = []
# while x==1:
#     res=requests.get(url=s)
#     a=res.text
#     # print(a)
#     b=re.findall('<i class="hq">(.*?)</i>',a)
#     f=re.findall('<i class="lq">(.*?)</i>',a)
#     c=re.findall('< a href=" ">下一页</ a>',a)
#     n=0
#     j=0
#     with open(path,"a+",encoding="utf-8") as h:
#         for i in range(0,len(b)):
#             n+=1
#             h.write(b[i]+" ")
#             if n==6:
#                 n=0
#                 h.write(f[j]+"\n")
#                 j+=1
#         j=0
#     if c!=d:
#         s=c[0]
#     else:
#         x=2
#         break


import requests
import re

# 链接地址
url = "https://www.ydniu.com/open/ssq-500/1.html"

# 请求头模拟浏览器
headers = {
    'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36", }
# 请求接口
res = requests.get(url=url, headers=headers, timeout=2)
data1 = res.text
# print(data1)
# 用正则提取尾页的页码
max_number = int(re.search('ssqa-500/(.*?)\.html\">尾页</a>', data1).group(1))
# 根据网页规则拼接每一页的URL
for i in range(1, max_number + 1):
    url1 = f"https://www.ydniu.com/open/ssq-500/{i}.html"
    print(f'访问的url为：{url1}')
    # 请求每一页获取返回结果
    res1 = requests.get(url=url1, headers=headers, timeout=2)
    data2 = res1.text
    # print(data2)
    # 正则提取 彩票号码
    # 每个号码的前6位数字组成一个列表
    number_list1 = re.findall('<i class="(hq|lq)">(.*?)</i>', data2)
    print(number_list1)
    datalist = []
    hlist, llist = [], []
    for i,j in number_list1:
        if i == 'hq':
            hlist.append(j)
        elif i == 'lq':
            llist.append(j)
            datalist = hlist+llist
            print(datalist)
            hlist, llist = [], []
            with open('data.txt', 'a+') as fp:
                fp.write(str(datalist).strip("'[").strip("]'").replace(',','').replace("'",'')+'\n')
