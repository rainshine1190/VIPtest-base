
#函数的参数：调用函数的时候，函数接受到的数

#参数传递1：位置传递

#全局变量
a = 1
b = 2

def add(a,b):
    #函数内部定义的变量都叫局部变量，都不能在函数外部引用
    return a + b

result = add(a,b)
print(result)