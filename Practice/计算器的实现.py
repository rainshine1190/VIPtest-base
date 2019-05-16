#coding:utf-8
# __author__ = 'lc'



def calc(x,y,z):
    if z=='+':
        return  x+y
    elif z=='-':
        return x-y
    elif z=='*':
        return x*y
    elif z=='/':
        if y==0:
            return 'error：除数不能为0'
        return  x/y
    else:
        return 'error：运算符号错误'

a=int(input('请输入第一个数字：'))
c=input('请输入需要的 + - * / 运算:')
b=int(input('请输入第二个数字：'))

print(calc(a,b,c))
