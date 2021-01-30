'''

    日志级别：
            CRITICAL
            ERROR
            WARNING
            INFO
            DEBUG

    日志配置：basicConfig，默认控制台输出

'''




#--------------------------封装成函数或类对外开放

#1、导入Logging包
import logging

def log():

    #2、设置基础配置信息(level：日志级别，格式：)
    logging.basicConfig(level=logging.INFO,format='%(asctime)s-%(name)s-%(levelname)s-%(message)s')

    #3、定义日志名称getlogger，在输出日志的时候显示
    logger = logging.getLogger("log_demo")

    return logger

#4、info,debug
# logger.setLevel("DEBUG")
# logger.setLevel(logging.INFO)
if __name__ == '__main__':
    logger = log()
    logger.debug("debug")
    logger.info("info")
    logger.warning("warning")