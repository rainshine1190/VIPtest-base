#coding:utf-8
__author__ = 'lc'


from selenium import webdriver
import time


def startBrowser():

    driver = webdriver.Chrome()
    driver.get("http://www.baidu.com")
    driver.maximize_window()
    time.sleep(5)
    driver.close()

startBrowser()












