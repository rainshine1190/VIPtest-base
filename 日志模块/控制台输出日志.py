
#1、导入Logging包
import logging


def log():
    #2、设置配置信息(level：日志级别，格式：)

    formatter = logging.Formatter('%(asctime)s-'
                                      '%(levelname)s-'
                                      '%(filename)s-'
                                      '%(threadName)s-'
                                      '[line:%(lineno)d]-'
                                      '%(name)s-'
                                      '日志信息：%(message)s')

    #3、定义日志名称getlogger，在输出日志的时候显示
    logger = logging.getLogger("log_demo")

    logging.basicConfig(level=logging.INFO, format='%(asctime)s-%(name)s-%(levelname)s-%(message)s')

    """设置控制台输出的句柄"""
    # ch = logging.StreamHandler()
    # ch.setLevel(logging.DEBUG)  # 指定被处理的信息级别为最低级DEBUG，低于level级别的信息将被忽略
    # ch.setFormatter(formatter)

    # logger.addHandler(ch)
    return logger

if __name__ == '__main__':
    logger = log()

    logger.info("what are you doing")