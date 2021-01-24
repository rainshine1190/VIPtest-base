str1 = 'hello'
for i in str1:
    if i == 'e':
        print('遇到e不不打印')
        continue
    print(i)
else:
    print('循环正常结束之后执⾏行行的代码')