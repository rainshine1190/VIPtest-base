# 数据库
list1 = [{'name': 'yangmingwei0', 'age': 18, 'sex': 'nan'}, {'name': 'yangmingwei1', 'age': 18, 'sex': 'nan'},
         {'name': 'yangmingwei2', 'age': 18, 'sex': 'nan'}, {'name': 'yangmingwei3', 'age': 18, 'sex': 'nan'}]


# 新增用户函数
def user_add(name, age, sex):
    """
    新增用户信息,如用户已存在则不新增并进行提示
    :param name:姓名
    :param age: 年龄
    :param sex: 性别
    :return: None
    """
    # 遍历列表判断用户是否已经存在,如已存在则进行提示,并退出循环
    for i in list1:
        if i["name"] == name:
            print("该用户已存在")
            break
    # 如不存在则进行新增
    else:
        msg = {"name": name, "age": age, "sex": sex}
        list1.append(msg)
        print("新用户添加成功-->", msg)


# 查询所有用户信息
def print_info():
    """
    查询所有学生信息
    :return: None
    """
    # 遍历打印学生信息
    for i in list1:
        print("学生信息：", i)


# 查询某个学生信息
def print_user(name):
    """
    查询某个学生信息,存在则打印学生信息,不存在则给出友好提示
    :param name: 学生姓名
    :return: None
    """
    # 遍历取指定学生信息,取到则打印并退出循环
    for i in range(len(list1)):
        if name == list1[i]["name"]:
            print("用户信息:", list1[i])
            break
    # 取不到给出友好提示
    else:
        print("您查询的用户不存在")


# 删除某个学生信息
def del_user(name):
    """
    删除指定学生信息
    :param name: 学生姓名
    :return:None
    """
    # 遍历判断学生是否存在,如果存在则删除并退出循环
    for i in range(len(list1)):
        if name == list1[i]["name"]:
            print("被删除用户信息:", list1.pop(i))
            break
    # 如果不存在则给出友好提示
    else:
        print("您要删除的用户不存在")


# 入口函数
def run():
    """
    学生信息系统入口函数
    :return:None
    """
    # 循环首页让用户进行对应操作选择
    while True:
        # 提示信息
        print('===================================')
        print('1-新增用户')
        print('2-查询用户')
        print('3-删除用户')
        print("4-查看所有用户")
        print("5-退出系统")
        print('===================================')
        # 进行功能选择
        n = input("请选择:")
        # 调用新增学生接口
        if n == "1":
            print("调用新增用户函数")
            name = input("请输入姓名：")
            age = int(input("请输入年龄："))
            sex = input("请输入性别：")
            user_add(name, age, sex)
        # 调用查询学生接口
        elif n == "2":
            print("调用查询用户函数")
            name = input("请输入要查询的学生姓名：")
            print_user(name)
        # 调用删除学生接口
        elif n == "3":
            print("调用删除用户函数")
            name = input("请输入要删除的学生姓名：")
            del_user(name)
        # 调用查询所有学生接口
        elif n == "4":
            print("调用查看所有用户函数")
            print_info()
        # 出口
        elif n == "5":
            break
        # 非法输入提示
        else:
            print("输入数据非法")


# 执行入口函数
run()
