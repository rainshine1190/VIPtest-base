import my_module1


try:
    f = open('test.txt')

    try:
        while True:
            content = f.readline()
            if len(content) == 0:
                break
            my_module1.sleep(2)
            print(content)
    except:
        # 如果在读取⽂文件的过程中，产⽣生了了异常，那么就会捕获到
        # ⽐比如 按下了了 ctrl+c
        print('意外终⽌止了了读取数据')
    finally:
        f.close()
        print('关闭⽂文件')
except:
    print("没有这个⽂文件")