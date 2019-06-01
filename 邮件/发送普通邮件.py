#coding:utf-8
__author__ = 'lc'

from smtplib import SMTP

# 发送html内容的邮件
import smtplib, time, os
from email.mime.text import MIMEText
from email.header import Header



def sendMail():

    '''发送html内容邮件'''
    #第一步：配置邮箱属性

    # 发送邮箱
    sender = 'rainshine1190@126.com'
    # 接收邮箱
    receiver = '421071642@qq.com'
    # 发送邮件主题
    t = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    subject = '自动化测试结果_' + t
    # 发送邮箱服务器
    smtpserver = 'smtp.126.com'
    # 发送邮箱用户/密码
    username = 'rainshine1190'
    password = '881109.com'
    content = 'Python 邮件发送测试...'

    #第二步： 组装邮件内容和标题，中文需参数‘utf-8’，单字节字符不需要
    msg = MIMEText(content, 'plain', 'utf-8')
    msg['Subject'] = Header(subject, 'utf-8')
    msg['From'] = sender
    msg['To'] = receiver

    #第三步：登录并发送邮件
    try:
        #1--实例化smtp类
        smtp = smtplib.SMTP()
        #2--连接stmp服务器
        smtp.connect(smtpserver)
        #3--登录邮箱
        smtp.login(username, password)
        #4--设置发件人，收件人，邮件内容
        smtp.sendmail(sender, receiver, msg.as_string())
    except:
        print("邮件发送失败！")
    else:
        print("邮件发送成功！")
    finally:
        smtp.quit()





#调试发送邮件
sendMail()

