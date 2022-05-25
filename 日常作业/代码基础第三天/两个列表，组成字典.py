"""
功能描述：有两个列表，一个存放的是学生姓名，一个存放的是学生的年龄，生成一个字典，key为姓名，value为年龄，要求只记录年龄大于20的学生姓名和年龄
编写人：liangchao
编写日期：
实现逻辑：

name = ['xiaoming','xiaohong','xiaohei']
age = [19,20,31]
得到：
{'xiaohong': 20, 'xiaohei': 31}

"""

name = ['xiaoming','xiaohong','xiaohei']
age = [19,20,31]
dict1 = {name[i]:age[i] for i in range(len(name))}
print(dict1)