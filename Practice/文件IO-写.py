#coding:utf-8
# __author__ = 'lc'



#------------------------------写入

f = open('E:\code\VIPtest2\data.txt','w+')

#写入文件内容，覆盖原有内容，将字符串写入文件，返回的是写入的字符长度。
# f.write('hello Python！')

# f.seek(0)
m = ['helo','world']

#向文件写入一个序列字符串列表，如果需要换行则要自己加入每行的换行符。
f.writelines(m)

f.seek(0)
print(f.read())

f.close()
