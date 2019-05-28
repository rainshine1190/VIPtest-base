#coding:utf-8
# __author__ = 'lc'

import pymysql
# def person(name,age,**kwargs):
#     print('****',name,age,kwargs)
#
#
# person('xiaoming',21,sex='male',color='blue')
# person('xiaoming',21)
# person('xiaoming',21,sex=1)
# # person('xiaoming',21,'male')



def person(**kwargs):
    host = kwargs['host']
    user = kwargs['user']
    pwd = kwargs['pwd']
    database = kwargs['database']
    port = int(kwargs['port'])

    db = pymysql.connect(host,user,pwd,database,port)
    cursor = db.cursor()
    cursor.execute('select  * from record limit 5')
    data = cursor.fetchall()
    print(data)
    # print('****',kwargs['host'])



db = {'host': '10.110.83.85', 'port': '4002', 'user': 'task_inyuapp_rw', 'pwd': 'gh31mllgcUrobfamdaWl', 'database': 'task_inyuapp'}
print(type(db))
person(**db)
# person('xiaoming',21)
# person('xiaoming',21,sex=1)
# # person('xiaoming',21,'male')


