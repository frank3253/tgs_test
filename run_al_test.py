import unittest, time
from HTMLTestRunner import HTMLTestRunner
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from tgs.test_case.model import config
from email.header import Header
import smtplib, os


# 发送测试报告，需要配置你的邮箱账号
def send_mail(file_new):
    # 读取配置文件

    # 发送邮件服务器
    smtpserver = "imap.exmail.qq.com"
    # 发送邮件
    sender = "yanhao@taogushen.com"
    # 接受邮件
    receiver = "yanhao@taogushen.com"
    # 发送邮箱账号/密码
    user = config.emailconfig( )[0]
    password = config.emailconfig( )[1]
    # 加载测试报告
    f = open(file_new, 'rb')
    mail_body = f.read( )
    f.close( )

    # 构造附件
    msg = MIMEText(mail_body, 'base64', 'utf-8')
    # 附件内容的类型
    msg["Content-Type"] = 'application/octet-stream'
    # 附件段体的安排方式
    msg["Content-Disposition"] = 'attachment; filename = "log.html"'

    # 构造邮件内容html类型
    msg1 = MIMEText(mail_body, 'html', 'utf-8')

    # 创建一个带附件的实例
    msgRoot = MIMEMultipart('related')
    msgRoot['Subject'] = "自动化测试报告"
    msgRoot['From'] = 'yanhao@taogushen.com'
    msgRoot['To'] = config.emailconfig( )[2]
    msgRoot.attach(msg1)
    msgRoot.attach(msg)

    # 邮件发送
    smtp = smtplib.SMTP( )
    smtp.connect(smtpserver)
    smtp.login(user, password)
    smtp.sendmail(sender, receiver, msgRoot.as_string( ))
    smtp.quit( )
    print('email has send out!')


# 查找测试报告目录，找到最新生成的测试报告文件
def new_report(testreport):
    # 获取文件列表
    lists = os.listdir(testreport)
    # 按时间排序
    lists.sort(key=lambda fn: os.path.getmtime(testreport + '\\' + fn))
    # 将多个路径组合后返回路径给file_new
    file_new = os.path.join(testreport, lists[-1])
    # print(file_new)
    return file_new


# 指定测试用例为当前文件夹下的test_case目录
# 指定测试报告的全路径
test_dir = './tgs/test_case'
discover = unittest.defaultTestLoader.discover(test_dir, pattern='case_01*.py')
test_report = "./tgs/report"

if __name__ == "__main__":
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = test_report + '/' + now + 'result.html'
    fp = open(filename, 'wb')
    # runner = unittest.TextTestRunner()
    runner = HTMLTestRunner(stream=fp,
                            title='测试报告',
                            description="运行环境：windows 10, Chrome")
    runner.run(discover)
    fp.close( )

    new_report = new_report(test_report)
    send_mail(new_report)
