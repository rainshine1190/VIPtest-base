"""
需求：有一堆字符串“aabbbcddef”打印出不重复的字符串结果：cef
分析：
    1-判断每个字符串出现的次数，为1的追加如空列表，输出
"""
str1 = 'aabbbcddef'
str2 = ''
for i in str1:
    if list(str1).count(i) == 1:
        str2 += i
print(str2)