# str1 = 'hello'
# for i in str1:
#     if i == 'e':
#         print('遇到e不不打印')
#         continue
#     print(i)
# else:
#     print('循环正常结束之后执⾏行行的代码')


a=int(input('斐波那契数列第几项？'))

def num(b):
    if b<=1:
        return b
    else:
        return (num(b-2)+num(b-1))


# print(num(a))

for i in range(a):
    print(num(i))