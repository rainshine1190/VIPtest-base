"""
功能描述：
编写人：
编写日期：
实现逻辑：

"""
# !/usr/bin/python
# -*- coding: UTF-8 -*-

import re

# result = re.findall('(\d+)', '010 是北京市的区号，110不是')
# print("match匹配后的对象为：", result)

# print("result.group()输出：", result.group())
# print("result.groups()输出：", result.groups())
# print("result.group(0)输出：", result.group(0))
# print("result.group(1)输出：", result.group(1))
# print("result.group(2)输出：", result.group(2))

#不带括号
# result = re.match('\d{3,4}', '010 是北京市的区号0351')
# print("match匹配后的对象为：", result)
#
# print("result.group()输出：", result.group())
# print("result.groups()输出：", result.groups())
# print("result.group(0)输出：", result.group(0))



#-------------findall

# import re
#
# kk = re.compile(r'\d+')
# print(kk)
# result = kk.findall('one1two2three3four4')
# print(result)


# 注意此处findall()的用法，可传两个参数;
# import re
#
# kk = re.compile(r'\d+')
# result = re.findall(kk, "one1two2three3four4")
# print(result)

# str1 = """
#     <body>
#         <div>
#             <span class="c-text c-text-hot opr-toplist1-label">橙好牛逼</span><a href='http://www.baidu.com'>百度</a>
#         </div>
#     </body>
#
# """
# #通过*匹配多个字符，通过？非贪婪匹配控制匹配到的内容为最少内容，不重复匹配<
# pat = re.compile('>(.*?)<')
# result = pat.findall(str1)
# print(result)
# print(result[0])


# import re
#
# str1 = "chenghaokeji666 chenghaokeji888 chenghaokeji1234 chenghaokeji6789"
#
# # 此处因为数字的数量都不统一，那么我们就要通过+来控制数字数量，表示1个多多个
# num = re.sub(r'[0-9]+', "***", str1)
# print("slogan: ", num )

# import re
#
# str1 = "chenghaokeji666 chenghaokeji888"
#
# # 此处因为数字的数量都是3个，通过\d表示单个数字完成统一替换，
# result = re.sub(r'\d+', "777", str1)
# print("slogan是: ", result)

#
# import re
#
# str1 = "chenghaokeji666 chenghaokeji888 chenghaokeji1234 chenghaokeji6789"
#
# # [0-9]表示匹配单个数字0-9,+匹配前面的字符1个多个数字
# result = re.search(r'[0-9]+', str1)
# print("匹配后的结果对象为: ", result)
# #
# print("group()获取表达式匹配到的整体结果: ", result.group())
# #因为正则表达式没有使用()分组，所以获取到的元组为空
# print("groups()获取一个包含所有小组字符串的元组：", result.groups())


# import re
#
# str1 = "chenghaokeji666 chenghaokeji888 chenghaokeji1234 chenghaokeji6789-0538"
#
# # [0-9]表示匹配单个数字0-9,+匹配前面的字符1个多个数字
# result = re.search(r'([0-9]+).*-(\d+$)', str1)
# print("匹配后的结果对象为: ", result)
# #
# print("group()获取表达式匹配到的整体结果:", result.group())
# print("group(1)获取第一组正则匹配到的结果", result.group(1))
# print("group(2)获取第二组正则匹配到的结果", result.group(2))
# print("groups()获取一个包含所有小组字符串的元组：", result.groups())


import re

str1 = "2018-05-31"

# [0-9]表示匹配单个数字0-9,+匹配前面的字符1个多个数字
result = re.search(r'^(\d{4})-(\d{2})-(\d{2})$', str1)
print("匹配后的结果对象为: ", result)
#
print("group()获取表达式匹配到的整体结果:", result.group())
print("group(1)获取第一组正则匹配到的结果", result.group(1))
print("group(2)获取第二组正则匹配到的结果", result.group(2))
print("group(2)获取第二组正则匹配到的结果", result.group(3))
print("groups()获取一个包含所有小组字符串的元组：", result.groups())
