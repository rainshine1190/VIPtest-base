"""
功能描述：
编写人：
编写日期：
实现逻辑：

需求：5-居中三角形1和2

  *     1行  1*  2空
 ***    2行  3*  1空
*****   3行  5*  0空

分析：
    i 从1----3 行数
    j * 数量    1 3 5
        行数和*数量的关系表达式：j = 2n -1
    h 空格 数量 2 1 0
        行数和空格数量的表达式：h = 3-i

"""
# n = int(input('please input your num:'))
#
# for i in range(1,n):
#     print((n-1-i)*' ' + (2*i-1)*'*')




"""


*****   3行  5*  0空
 ***    2行  3*  1空
  *     1行  1*  2空
  
分析：
    i 从1----3 行数
    j * 数量    1 3 5
        行数和*数量的关系表达式：j = 2n -1
    h 空格 数量 2 1 0
        行数和空格数量的表达式：h = 3-i


"""

n = int(input('please input your num:'))

for i in range(n,0,-1):
    print((n-i)*' ' + (2*i-1)*'*')


"""

  *     
 ***    
*****   
 ***    
  *     

分析：
    上下三角形拼接罗列即可


"""

# n = int(input('please input your num:'))
#
# for i in range(1, n):
#     print((n - 1 - i) * ' ' + (2 * i - 1) * '*')
# for i in range(n - 2, 0, -1):
#     print((n - 1 - i) * ' ' + (2 * i - 1) * '*')