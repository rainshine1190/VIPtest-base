"""
需求：文件备份，将data.txt文件备份

分析：
    1-打开data.txt文件 f1 = open(data.txt,r)
    2-读data.txt文件的内容readlines()
    3-创建一个新文件data_backup.txt f2 = open(data_backup.txt, w)
    4-将第二步读取出来的内容写入到新文件中 f2.write()
        4.1 通过for 循环遍历 readlines读取出来的列表
            f2.write(i)

"""