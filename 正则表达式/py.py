def fun(n):
    if n <= 1:
        return n
    else:
        return fun(n-1) + fun(n-2)

# 测试
num = 500  # 设置要生成的斐波那契数列的项数

print("斐波那契数列:")
for i in range(num):
    print(fun(i))
