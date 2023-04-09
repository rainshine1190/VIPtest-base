"""
功能描述：
编写人：liangchao
编写日期：
实现逻辑：
导包
    1-
    2-
    3-

"""
# 1. if练习--从键盘输入一个数，判断该数是否在列表中，如果在就打印happy
# 2. if-else练习—从键盘输入一个数，判断该数是否在列表中，如果在就打印happy，并且让列表中的该值+1，否则打印sad
# 3. 输入一个数，判断该数的范围：90-100：等价为A……60以下：等级为E
# 4. 求10阶乘
# 5. 求100以内能被3整除的数，并将作为列表输出
# 6. 列表[1,2,3,4,3,4,2,5,5,8,9,7],将此列表去重，得到一个唯一元素的列表
# 7. 求斐波那契数列 1 1 2 3 5 8 13 ……
# 8. 文件data.txt内存在以下内容（每行采用逗号分隔）
# lucy:21，tom:30
# xiaoming:18，xiaohong:15
# xiaowang:20，xiaohei:19
# 输出年龄大于18岁的人名
strs = """
lucy:21，tom:30
xiaoming:18，xiaohong:15
xiaowang:20，xiaohei:19
"""
with open("datas.txt",'w+') as fp:
    fp.write(strs)
    fp.seek(0)
    res = fp.read()
    result = res.replace('，',',')
    goal = result.replace('\n',',')
    results = goal.strip(',')
    list1 = results.split(',')
    for i in list1:
        if int(i.split(':')[1])>18:
            print(i.split(':')[0])

# 13. 有一堆字符串，“welocme to super&Test”，打印出emcolew ot  ……全部单词原位置反转

# 14. 实现斐波那契数列，一种递归，一种其他方法
# 15. 求100以内的质数（只能被1和它本身整除）
# 16. 有一堆字符串“aabbbcddef”打印出不重复的字符串结果：cef
# 17. 有一堆字符串，“welocme to super&Test”，打印出superTest，不能查字符的索引
# 18. 有一堆字符串，“welocme to super&Test”，打印出tseT&repus ot ……全部单词原位置反转
# 19. 有一堆字符串，“abcdef”，将收尾反转，结果：fedcba，不能使用现有的函数或方法，自己写算法实现
# 20. 有一堆字符串，“aabbbcddef”，输出abcdef