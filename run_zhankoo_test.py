from HTMLTestRunner import HTMLTestRunner
import time
import os
import unittest
import smtplib
from email.mime.text import MIMEText
from email.header import Header

#发送邮件
def send_mail(report):
    f = open(report, 'rb')
    mail_body = f.read()
    f.close()

    msg = MIMEText(mail_body, 'html', 'utf-8')
    msg['Subject'] = Header('展酷自动化测试报告', 'utf-8')


    smtp = smtplib.SMTP()
    smtp.connect('smtp.163.com')
    smtp.login('iron_ly@163.com', '1227wdZ!')
    smtp.sendmail('iron_ly@163.com', 'linyang@zhankoo.com', msg.as_string())
    smtp.quit()

#获取最新测试报告文件
def new_report(report_path):
    report_list = os.listdir(report_path)
    report_list.sort(key=lambda x : os.path.getmtime(report_path + '\\' + x))
    file_new = os.path.join(report_path, report_list[-1])
    return file_new



if __name__ == '__main__':
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    base_dir = os.getcwd()
    base = base_dir.split('\\test_case')[0]
    filename = base + '\\report\\' + now + '_result.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp, title='展酷网自动化测试报告', description='环境：win7')
    discover = unittest.defaultTestLoader.discover(base + '\\test_case',pattern='*_sta.py')
    runner.run(discover)
    fp.close()
    report_file = new_report(base + '\\report')
    # send_mail(report_file)

