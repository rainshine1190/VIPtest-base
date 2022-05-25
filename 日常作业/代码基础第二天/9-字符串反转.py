'''

需求：abcdef

    fedcba

    a f
    tmp
    tmp  = list
    f =
    a = tmp


    a = 1 b = 2
    c = a
    a = b
    b = c

'''

str1 = 'abcdef'
str2 = list(str1)
n = 0
#首尾替换，只需要替换到中间即可，否则会出现重复替换的bug
while n < len(str2)/2:
    #-----下面的三个变量互相替换的三行代码可以简写成：a,b = b,a 就可以实现a和b变量的替换
    tmp = str2[n]
    str2[n] = str2[len(str2)-n-1]
    str2[len(str2)-n-1] = tmp
    n += 1

print(str2,str1)
print(''.join(str2))