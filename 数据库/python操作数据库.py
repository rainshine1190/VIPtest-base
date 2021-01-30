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



#打开数据库连接
conn = pymysql.connect('localhost',user = "root",passwd = "123456",db = "testdb")

#获取游标
cursor=conn.cursor()
