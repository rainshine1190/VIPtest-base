'''
列表[1,2,3,4,3,4,2,5,5,8,9,7],将此列表去重，得到一个唯一元素的列表


分析：
    1-count
    2-判断是否在空列表中是否存在
    if i not in K_list:
        k_list.append(i)



'''

list1 = [1,2,3,4,3,4,2,5,5,8,9,7]
list2 = []

for i in list1:
    if i not in list2:
        list2.append(i)

print(list2)