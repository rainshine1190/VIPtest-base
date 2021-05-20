'''
功能描述：python操作数据库mysql
编写人：
编写日期：

步骤分析：
    1-
    2-
    3-
'''


#导包，python3使用pymysql，启用mysqldb
import pymysql

#1连接数据库
conn = pymysql.connect(host='localhost',user = "root",password = "",db = "test")

#2获取游标
cursor=conn.cursor()

# #3准备要执行的sql
# sql = 'SELECT * from user_info where id = 1 or id = 2 or id = 3'
# #4执行sql
# cursor.execute(sql)
#
# #5获取sql结果
# # fetch的每个方法都会导致游标动，比如fetchall操作完后如果继续用fetchone会输出none，
# # 因为游标已经到达返回结果的最后，所以如果想继续使用fetchone，则建议单独调试，不要批量使用，所以必须注意游标的位置。
# # print('fetchall的输出结果：',cursor.fetchall())
# print('fetchone的输出结果：',cursor.fetchone())
# # print('fetchmany的输出结果：',cursor.fetchmany(2))
# #关闭游标
# cursor.close()
# #关闭连接
# conn.close()

# #3准备要执行的sql
# sql = 'SELECT * from user_info where id = %s or id = %s or id = %s'
# #4执行sql，通过args传参，实现动态参数传递
# cursor.execute(sql,args=(1,2,3))
# #5获取sql结果
# print(cursor.fetchone())	#返回一个元组，元组的内容就是sql的第一行结果(1, 'xys', 20, '')

# #准备要执行的sql
# sql="insert into user_info values(%s,%s,%s,%s)"
# #4执行sql
# insert = cursor.executemany(sql,args=[(14, 'xys', 20,''), (15, 'a1', 21,''), (16, 'b1', 23,'')])
#
# #获取sql结果
# print('添加语句受影响的行数：',insert)
#
# #注意：最后必须提交操作，否则写操作（更新，修改，删除，新增）不生效
# conn.commit()


#查询插入的数据
#获取游标
# cursor=conn.cursor()
# sql = 'select * from user_info order by id desc limit 3'
# cursor.execute(sql)
#
# cursor.close()
# conn.close()
# print(cursor.fetchall())


# #更新一条数据
# update=cursor.execute("update user_info set age=11 where id=2")
# print ('更新后受影响的行数为：',update)
# conn.commit()
# #查询一条数据
# cursor.execute('select * from user_info where id = 2;')
# print('更新后的查询结果',cursor.fetchall())
#
# #关闭游标
# cursor.close()
# #关闭连接
# conn.close()


# #更新多条数据
# sql="update user_info set age = %s where id = %s"
# update=cursor.executemany(sql,[(22,2),(23,3)])
# conn.commit()
# print ('更新后受影响的行数为：',update)
# #更新后查询数据
# cursor.execute('select * from user_info where id = 2 or id = 3;')
# print('更新后的查询结果',cursor.fetchall())
#
#
# conn.close()


# # 删除操作
# # 删除1条数据
# sql = "delete from user_info where id = %s"
# delete = cursor.execute(sql,(2))
# conn.commit()
# print ('删除后受影响的行数为：',delete)
# #删除后查询数据
# cursor.execute('select * from user_info where id = 2')
# print('删除后的查询结果',cursor.fetchall())


#删除操作
#删除多条数据
# sql = "delete from user_info where id = %s"
# delete = cursor.executemany(sql,(7,8,9))
# conn.commit()
# print ('删除后受影响的行数为：',delete)
# #删除后查询数据
# sql = 'select * from user_info where id in (7,8,9)'
# cursor.execute(sql)
# print('删除后的查询结果',cursor.fetchall())
#
# conn.close()



#插入操作

# insert=cursor.execute("insert into user values(1,'tom',18)")
# print('添加语句受影响的行数：',insert)

# #插入一条数据
# sql="insert into user_info values(%s,%s,%s,%s)"
# insert = cursor.execute(sql,(24,'kongsh',20,''))
# print ('插入后受影响的行数为：',insert)
# #插入后查询该数据
# sql = 'select * from user_info where id = 24'
# cursor.execute(sql)
# print('插入后的查询结果',cursor.fetchall())
#
# conn.close()


#插入多条数据
sql="insert into user_info values(%s,%s,%s,%s)"
insert = cursor.executemany(sql,[(25,'kongsh1',20,''),(26,'kongsh2',20,'')])
conn.commit()
print ('插入后受影响的行数为：',insert)
#插入后查询该数据
sql = 'select * from user_info where id = 25 or id = 26'
cursor.execute(sql)
print('插入后的查询结果',cursor.fetchall())

conn.close()


#新建表

#
# sql = """CREATE TABLE `user_info1` (
#   `id`   BIGINT(20)  NOT NULL AUTO_INCREMENT,
#   `name` VARCHAR(50) NOT NULL DEFAULT '',
#   `age`  INT(11)              DEFAULT NULL,
#  `sfzh` char(18) not null DEFAULT '',
#   PRIMARY KEY (`id`),
#   KEY `name_index` (`name`)
# )ENGINE = InnoDB DEFAULT CHARSET = utf8;"""
#
# create = cursor.execute(sql)
# conn.commit()
# print ('新建后受影响的行数为：',create)
# #插入后查询该数据
# #关闭游标
# cursor.close()
# #关闭连接
# conn.close()