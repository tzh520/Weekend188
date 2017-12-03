import os
import smtplib
import unittest
# HTMLTestRunner 是基于unittest框架的一个扩展，可以自己在网上搜索下载，注意区分python版本
import time
from email.header import Header
from email.mime.text import MIMEText

from lib.HTMLTestRunner import HTMLTestRunner


def send_mail(path):
    f = open(path, 'rb') # html文档不是普通的文档，需要用二进制的方式读
    mail_body = f.read() # 读取html报告的内容，作为邮件的正文
    
    f.close()

    # 要想发邮件，我们要把二进制的内容转成MIME格式
    # MIME multipurse多用途 Internet 互联网 Mail 邮件 Extension 扩展
    # MIME是对邮件协议的一个扩展，使邮件不仅支持文本格式，还支持多种格式，如图片，音频，二进制文件等
    # 将mail_body转换成html的编码格式是utf-8的文件
    msg = MIMEText(mail_body, 'html', 'utf-8')
    # smg是邮件的正文，但对一个邮件来讲，除了正文，还需要主题，发件人，收件人
    # 设置邮件的主题，Subject 主题
    # msg是字典的类型，字典类似于数组，区别是：1.字典是无序的；
    msg['Subject'] = Header('自动化测试报告', 'utf-8')
    # 如果想用客户端软件或者自己写代码登录邮箱，很多类型的邮箱服务器需要单独设置一个客户端授权码，为了邮箱安全着想
    # 设置发件箱和收件箱
    msg['From'] = 'bwftest126@126.com'
    msg['To'] = 'tianzhihui0@163.com'

    # 现在邮件内容已经准备好了，下面开始发送邮件
    # 发邮件手动步骤：
    # 1.打开登录页面，即连接邮箱服务器
    # 要想连接服务器，首先必须搞清楚网络传输协议
    # http，https，ftp，socket
    # 发邮件的协议一般有三种，你要先查看你的邮箱是哪种协议
    # 126邮箱支持这三种协议pop3，smtp，imap
    # 我们要选一种传输协议用来发邮件，smtp
    # smtp simple mail transful protocol 简单邮件传输协议
    # 首先导入smtplib的代码库
    smtp = smtplib.SMTP() # 实例化一个SMTP的对象
    smtp.connect('smtp.126.com') # 连接126邮箱的服务器地址
    # 2.登录邮箱
    smtp.login('bwftest126@126.com','abc123asd654')
    # 3. 发送邮件
    smtp.sendmail('bwftest126@126.com', 'tianzhihui0@163.com', msg.as_string())
    # 4.关闭邮箱
    smtp.quit()
    print("Email has send out!")


if __name__ == '__main__':
    # str String  f format
    # strftime 格式化的时间，通过strftime()这个方法可以定义时间的格式
    # Y year年， m month月， d day日， H hour 小时， M minute分， S second秒
    # 因为时间要加到文件名里，但文件名不能用冒号，所以时分秒中间用-
    now = time.strftime("%Y-%m-%d_%H-%M-%S")

    suite = unittest.defaultTestLoader.discover("./day5", "*Test.py")
    # unittest.TextTestRunner().run(suite) 文本测试用例运行器
    # 现在用html的测试用例运行器
    # html的测试用例运行器 最终会生成一个html格式的测试报告
    # 我们至少要指定测试报告的路径
    # stream 流 sys.stdout 系统标准输出，也就是二进制输出
    base_path = os.path.dirname(__file__)
    path = base_path + "/report/report" + now + ".html"
    file = open(path, "wb")
    HTMLTestRunner(file, 1, "海盗商城测试报告", "测试环境：window server 2008 + Chrome").run(suite)
    # file.close()
    # 我们要把html报告作为邮件正文，发送给关心测试结果的人
    send_mail(path)
    # HTMLTestRunner(stream=file).run(suite)
    # 这时生成的测试报告，只显示类名和方法名，只能给专业的人士看
    # 我们应该把相关的手动测试用例的标题加到我们的测试报告里
    # 我们自动化测试用例是从手工测试用例中挑出来的，手工测试用例怎么写我们就怎么编写代码，所以我们的代码里应该能体现手工测试用例的标题
    # 新的测试报告会覆盖原来的测试报告，如果想把所有的测试报告保存起来怎么做？
    # 加一个时间戳，按照当前时间计算一个数字，将数字作为文件名的一部分，那么就避免了文件名重复的问题
    # 现在我们的html格式的测试报告生成了，当测试用例全部执行完成，我们应该生成一封提醒邮件，通知所有关心测试结果的人






