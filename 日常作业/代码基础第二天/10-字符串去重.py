"""
需求：有一堆字符串“aabbbcddef”打印出不重复的字符串结果：cef

分析：
    取count()次数=1的元素

"""
str1 = "aabbbcddef"
str2 = ""

for i in str1:
    if str1.count(i) == 1:
        str2 += i
print(str2)