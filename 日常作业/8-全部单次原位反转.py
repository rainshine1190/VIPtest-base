"""
有一堆字符串，“welocme to super&Test”，打印出tseT&repus ot ……全部单词原位置反转

分析：
    1-实现单个字符串反转
        1.1-首尾互换
        1.2-互换完追加到空列表中
    2-遍历所有字符串
        2.1-输出全部反转后的字符串，倒叙


"""
str1 = 'welocme to super&Test'
str2 = []
for i in str1.split(' '):
    i = list(i)
    #实现单个字符串反转
    n = 0
    while n < len(i)/2:
        i[n],i[len(i)-n-1] = i[len(i)-n-1],i[n]
        n += 1
    # 将反转后字符串拼接，然后追加到新列表中
    str2.append(''.join(i))
    # 倒叙输出并通过空格隔开每次反转后的字符串
result = ' '.join(str2[::-1])
print(result)