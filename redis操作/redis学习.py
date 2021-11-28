"""
功能描述：
编写人：liangchao
编写日期：
实现逻辑：
导包
    1-
    2-
    3-

"""
import time

import  redis

import redis,time

client = redis.Redis(host='192.168.3.128', port=6379)

# data = {'name1':'liang','name2':'chao'}
# client.mset(data)
#
# # client.msetnx()
# client.psetex('n',3,'n3')
# print(client.mget('n'))
# time.sleep(3)
# client.mset({'name3':'1','name4':'2'})
# client.delete('name1','name2')
# print(client.mget('name1','name2'))


# client.set("foo", 123)
# print(client.get("foo"))
# client.incr("foo")
# print(client.mget("foo"))
print(client.get("foo4"))
client.decr("foo4",3) # 递减3
print(client.get("foo4"))
client.decr("foo10","foo11") # 递减1
print(client.mget("foo10","foo11"))
