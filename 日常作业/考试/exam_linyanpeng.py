'''
基础考试试卷

期数 ：

说明：线上考试，请大家自觉，不要作弊，可以使用本地pycharm编程，然后复制到txt中

'''

'''
1.python的数据类型都有哪些(5分)
 整型：int
 字符串：str
 浮点型：float
 布尔：bool
 元组：tuple
 字典：dict
 列表：list
 集合：set

2.列表，元组、字典、集合如何定义，分别举例（5分）
列表：list1 = ['1','a','123']
元组：tuple1 = (1,'a','b')
字典：dict1 = {'name' : 'Tom','age' : '18'}
集合：set1 = {3,1,6}
'''

# 3.列表[1, 2, 3, 4, 5, 5, 2, 3, 2, 4]去重，不能使用现有函数（10分）
list1 = [1, 2, 3, 4, 5, 5, 2, 3, 2, 4]
list2 = []
for i in list1:
    if i not in list2:
        list2.append(i)
print(list2)

# 4.比如有这样一个文件data.txt内存在以下内容（每行采用逗号分隔）（15分）
# ----------------------------
# lucy: 21，tom: 30
# xiaoming: 18，xiaohong: 15
# xiaowang: 20，xiaohei: 19
# ----------------------------
# 请通过代码读取文件并输出年龄大于18岁的人名
f = open("data.txt","r",encoding="utf-8")
list1 = f.readlines()
f.close()
list2 = []
# print(list1)
for i in list1:
    list2.extend(i.split('，'))
# print(list2)
list3 = []
for x in list2:
    list3.append(x.replace('\n',''))

# print(list3)
for y in list3:
    name,age = y.split(':')
    if int(age) > 18:
        print(name)



# 5.请用列表推导式得出1 - 100能被3整除的数（5分）
list1 = [i for i in range(1,101) if i % 3 == 0]
print(list1)

'''
6.continue和break的区别（5分）
continue是结束本次循环，开始下次循环，需要注意continue前循环变量要先发生变化
break是直接退出循环
'''

# 7.有一堆字符串，“welocme to super&Test”，打印出emcolewottseT & repus……全部单词原位置反转，不能使用索引倒序输出或者通过其他现有函数实现，自己写字符串首尾交换方法（15分）
str1 = 'welocme to super&Test'
list1 = str1.split(' ')
list3 = []
for i in list1:
    list2 = list(i)
    for x in range(len(list2) // 2):
        list2[x], list2[-x - 1] = list2[-x - 1], list2[x]
    list3.append(''.join(list2))
print(' '.join(list3))

'''
8.怎么在函数内修改 / 使用全局变量（5分）
global 变量名  #声明全局变量

9.python可变数据类型和不可变数据类型都有哪些（5分）
可变数据类型：列表、字典、集合
不可变数据类型：整型、浮点型、字符串、元组、布尔
'''


# 10.递归实现斐波那契数列（10分）
def feibo(n):
    if n == 1 or n == 2:
        return 1

    else:
        return (feibo(n - 1) + feibo(n - 2))


# num1 = feibo(6)
# print(num1)
for i in range(1,10):
    print(feibo(i))

'''
11、debug的快捷键：f8 / f7 / f9分别的作用（5分）
f8:在单步执行时，在函数内遇到子函数时不会进入子函数内单步执行，而是将子函数整个执行完再停止
f7:在单步执行时，在函数内遇到子函数时会进入子函数内单步执行
f9:不会单步执行，一直执行到断点处才会停
'''

# 12、如何实现[‘1’, ’2’, ’3’]变成[1, 2, 3] ?（5分）
list1 = ['1', '2', '3']
list2 = []
for i in list1:
    x = int(i)
    list2.append(x)
print(list2)

# 13、开发一个注册系统，界面可以用print打印，保存用户名和密码，存在的用户提示已注册，不存在的可以注册成功（提示建议使用函数划分不同的功能，比如查询用户，新增用户）（10分）

list1 = []


def add_student():
    stu_name = input('请输入学生姓名：')
    stu_age = input('请输入学生年龄：')
    global list1
    for i in list1:
        if stu_name == i['name']:
            print('此学生已存在，无法添加')
            return
    dict1 = {}
    dict1['name'] = stu_name
    dict1['age'] = stu_age
    list1.append(dict1)
    print(list1)


def find_student():
    stu_name = input('请输入要查找的学生姓名:')
    global list1
    for i in list1:
        if stu_name == i['name']:
            print(f"您所查找的学生姓名为{i['name']}，年龄为{i['age']}")
            return
    print('学生信息不存在')


def del_student():
    stu_name = input('请输入要删除的学生姓名:')
    global list1
    for i in list1:
        if stu_name == i['name']:
            list1.remove(i)
            print(f"('学生{i['name']},已经删除')")
            break
    else:
        print('要删除的学生不存在')


def show_menu():
    menu_num = int(input('请选择您要使用的功能，1代表添加学生，2代表查找学生，3代表删除学生'))
    if menu_num == 1:
        add_student()
    elif menu_num == 2:
        find_student()
    elif menu_num == 3:
        del_student()
    else:
        print('请输入正确的功能选项')


show_menu()