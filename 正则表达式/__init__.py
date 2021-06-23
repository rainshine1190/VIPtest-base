"""
功能描述：
编写人：
编写日期：
实现逻辑：

"""

list1=[]#定义一个列表
def zhuce():#定义函数注册
    global list1 #声明是全局变量
    n=input("请用户输入名字")#接收用户名字
    p=input("请用户输入密码")#接收用户密码
    for  i in list1:#循环列表
        if i['name']==n: #判断是不是有相同的name
            break  #有就跳出循环
    else:
        add(n,p)#没有就添加用户
    return 0

def add(n,p):#添加函数
    dict1={}#定义空字典
    while True:#死循环
         dict1['name']=n#列表变身字典
         dict1['password']=p
         list1.append(dict1)#将字典添加到列表
         r=int(input("是否继续添加用户，继续1，不继续0\n"))#接收用户输入判断是否继续 添加用户
         if r==0:
             break
         else:
             zhuce()

zhuce()

