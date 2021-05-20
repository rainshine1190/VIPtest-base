#coding:utf-8
__author__ = 'lc'


from selenium import webdriver
import my_module1


def startBrowser():

    driver = webdriver.Chrome()
    driver.get("http://www.baidu.com")
    driver.maximize_window()
    my_module1.sleep(5)
    driver.close()

startBrowser()












