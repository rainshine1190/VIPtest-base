import smtplib
from email.mime.text import MIMEText
from email.header import Header


#------------------------配置邮件属性---------------------------------
# 发送方邮箱
sender = 'rainshine1190@126.com'
# 收件人邮箱，多个可以使用list，单个如下
# msg_to = ['****@qq.com','**@163.com','*****@163.com']
receiver = '421071642@qq.com'  # 单个收件人邮箱
#发送方邮箱账号，非邮箱全称
username = 'rainshine1190'
#发送方邮箱密码
password = 'xxx'  # 填入发送方邮箱的授权码(填入自己的授权码，相当于邮箱密码)
#发送方邮箱的服务器，每种邮箱服务器不同，具体可以百度
smtpserver = 'smtp.126.com'


#------------------------定义邮件最终配置信息---------------------------------
#邮件主题
subject = "邮件标题"
#邮件内容
content = "邮件内容，我是邮件内容，哈哈哈"
#
# 生成一个MIMEText对象（还有一些其它参数）
msg = MIMEText(content)
#或
msg = MIMEText(content,'plain','utf-8')
# 放入邮件主题
msg['Subject'] = subject
# 也可以这样传参
# msg['Subject'] = Header(subject, 'utf-8')
# 放入发件人
msg['From'] = sender
# 放入收件人
msg['To'] = receiver

#------------------------建立连接，发送邮件---------------------------------
try:
    # 通过ssl方式发送，服务器地址，端口
    s = smtplib.SMTP()
    s.connect(smtpserver)
    # 登录到邮箱
    s.login(username, password)
    # 发送邮件：发送方，收件方，要发送的消息通过as_string来作为字符串传递
    s.sendmail(sender, receiver, msg.as_string())
    print('成功')
except s.SMTPException as e:
    print(e)
finally:
    s.quit()