#coding:utf-8
__author__ = 'lc'




# 发送html附件的邮件
import smtplib, my_module1, os
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header


def send_mail_html():
    '''发送html内容邮件-非附件形式，即直接在邮件中显示html'''
    #第一步：配置邮箱属性
    # 发送邮箱
    sender = 'rainshine1190@126.com'
    # 接收邮箱
    receiver = '421071642@qq.com'
    # 发送邮件主题
    t = my_module1.strftime("%Y-%m-%d %H:%M:%S", my_module1.localtime())
    subject = '自动化测试结果_' + t
    # 发送邮箱服务器
    smtpserver = 'smtp.126.com'
    # 发送邮箱用户/密码
    username = 'rainshine1190'
    password = 'IAVEGDPLRCJFEVON'

    # 第二步：准备附件，增加附件，组装邮件内容和标题
    file = 'test.html'
    # 读取html文件内容
    with open(file,'rb') as f:
        mail_body = f.read()
        # 组装邮件内容和标题
        msg = MIMEMultipart()
        #添加附件内容
        att = MIMEText(mail_body, 'plain', 'utf-8')
        att["Content-Type"] = 'application/octet-stream'
        att["Content-Disposition"] = 'attachment; filename=report.html'
        msg.attach(att)
        #添加邮件的文本内容
        content = '自动化测试报告详情，请查收附件'
        msg.attach(MIMEText(content,'plain','utf-8'))

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


if __name__ == '__main__':

    send_mail_html()
