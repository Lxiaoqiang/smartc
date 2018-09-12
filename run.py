author = 'damao'

import unittest
from BeautifulReport import BeautifulReport
from common.send_mail import SendMail
import time
import os
from logs import my_logger
import shutil


logger = my_logger.LogHandler("python").getlog()

logger.info("running...")
now = time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time()))  # 获取当前时间
# print(now)
testcase_path = ".\\testcase\\"   # 测试用例的目录
logger.info("测试用例的目录:{a}".format(a=testcase_path))
report_path = ".\\report\\report_file\\"  # 测试报告目录
logger.info("测试报告目录:{a}".format(a=report_path))
logs_path = ".\\logs\\log_file\\"  # 日志文件目录
zip_log = ".\\logs\\zip_log\\"  # log打包目录
zip_report = ".\\report\\zip_report\\"  # 报告打包目录
send_mail_list = ["306936010@qq.com","1820832157@qq.com","cq154@zcsmart.com"]

def get_file_count(file_path):
    """获取指定文件夹下的文件数量"""
    number = 0
    for root,dirname,filenames in os.walk(file_path):
        for filename in filenames:
            # print(filename)
            if os.path.splitext(filename)[1] == '.log':
               number += 1
            elif os.path.splitext(filename)[1] == '.html':
                number += 1
    return number
    # 当文件数大于10时剪切文件到指定目录

def zip_file(old_path,new_path):
    if get_file_count(old_path) >= 10:
        for root, dirs, files in os.walk(old_path):
            for i in range(len(files)):
                # print(files[i])
                if (files[i][-4:] == '.log')or (files[i][-5:] == '.html'):
                    file_path = old_path + files[i]
                    # print(file_path)
                    new_file_path = new_path  #+ files[i]
                    # print(new_file_path)
                    try:
                        shutil.move(file_path, new_file_path)
                        logger.info("{a}条剪切成功！".format(a=i))
                    except Exception as e:
                        logger.info("剪切失败：{a}".format(a=e))
    else:
        print("文件少于10条，不需要剪切！")

def create_test_suite():
    """创建测试用例集"""
    test_suite = unittest.defaultTestLoader.discover(testcase_path,pattern='test_my_demo.py')
    logger.info("创建测试用例集:{a}".format(a=test_suite))
    return test_suite

"""执行方法"""
def run():
    test_suite = create_test_suite()
    result = BeautifulReport(test_suite)
    report_file_name = "接口测试报告" + now
    result.report(filename=report_file_name,description="接口自动化测试报告",log_path=report_path)
    # 发送测试报告给指定人

    sender = SendMail(smtp_server="mail.zcsmart.com",
                     smtp_port=993,
                     smtp_sender="cq154@zcsmart.com",
                     smtp_senderpassword="ai102839.",
                     smtp_receiver=send_mail_list,
                     smtp_subject="大毛的自动化测试邮件",
                     smtp_body="<p>接口测试报告：</p>",
                     smtp_file= '.\\Report\\report_file\\{a}.html'.format(a=report_file_name))
    sender.send_mail()
    logger.info("邮件发送成功！")
    # 自动判定日志文件及报告文件的个数，若超过10条就剪切之备份文件夹，少于10条不剪切
    zip_file(report_path, zip_report)  # 测试报告
    zip_file(logs_path, zip_log)  # 日志
    # 制定完毕后自动打开测试报告
    try:
        os.system(r'C:\softuser\FireFox\firefox.exe .\Report\report_file\{a}.html'.format(a=report_file_name))
    except Exception as e:
        logger.error("打开报告异常:{a}".format(a=e))


if __name__ == "__main__":
    run()
