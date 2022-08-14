"""
功能描述：
编写人：liangchao
编写日期：
实现逻辑：
导包
    1-遍历列表中的每一个元素，
    2-让每一个元素和后面的所有元素比较大小
        2.1-如果当前值大于下一个元素，则更换两个的位置
        2.2-否则继续比较下一个元素
    3-将所有元素遍历完成之后结束

"""
#-------------梁超排序
list1 = [1,3,2,8,9,4,5,7,6]

for i in range(len(list1)):
    for j in range(i+1,len(list1)):
        if list1[i] > list1[j]:
            list1[i],list1[j] = list1[j],list1[i]

print(list1)

#---------------冒泡排序
list1 = [1,3,2,8,9,4,5,7,6]

for i in range(len(list1)):
    for j in range(0,len(list1)-i-1):
        if list1[j] > list1[j+1]:
            list1[j],list1[j+1] = list1[j+1],list1[j]

print(list1)