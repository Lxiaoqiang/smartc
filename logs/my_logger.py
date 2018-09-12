author = 'damao'

import logging
import sys
import time

"""
日志级别排序：critical > error > warning > info > debug

debug : 打印全部的日志,详细的信息,通常只出现在诊断问题上
info : 打印info,warning,error,critical级别的日志,确认一切按预期运行
warning : 打印warning,error,critical级别的日志,一个迹象表明,一些意想不到的事情发生了,或表明一些问题在不久的将来(例如。磁盘空间低”),这个软件还能按预期工作
error : 打印error,critical级别的日志,更严重的问题,软件没能执行一些功能
criticl : 打印critical级别,一个严重的错误,这表明程序本身可能无法继续运行
"""
class LogHandler(object):
    def __init__(self,logger=None):
        # 获取logger实例
        self.logger = logging.getLogger(logger)
        # 设置日志的最低级别，默认是warning级别
        self.logger.setLevel(logging.DEBUG)  # 设置日志级别为debug级别
        # 文件日志
        self.now = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time()))  # 获取当前时间
        self.log_file_name = 'auto_test_' + self.now + '.log'
        # 指定logger输出格式
        formatter = logging.Formatter('[%(name)-4s %(asctime)s %(filename)s %(module)s  %(levelname)s] ===》 %(message)s')
        # log_file_path = '..\\logs\\'
        # print(log_file_name)
        log_file_handler = logging.FileHandler('.\\logs\\log_file\\{a}'.format(a=self.log_file_name),mode='w',encoding='utf-8') # 写入日志文件到本地
        log_file_handler.setFormatter(formatter) # 设置日志输入格式
        # 控制台日志
        console_handler = logging.StreamHandler(sys.stdout)  # 控制台输出日志
        console_handler.formatter = formatter  # 设置控制台输出的格式
        # 为logger添加日志处理器
        self.logger.addHandler(log_file_handler) # 日志文件处理器
        self.logger.addHandler(console_handler) # 控制台处理器
        # # 用pop把logger的handler列表中的handler移除
        # self.logger.handlers.pop()  # 解决日志打印重复的问题
        # 关闭打开的文件
        log_file_handler.close()
        console_handler.close()

    def getlog(self):
        return self.logger




if __name__ == "__main__":
    a = LogHandler("damao").getlog()
    # 输出不同级别的log
    a.debug('this is debug infosad打 第三方 发')
    a.info('this is information')
    a.warn('this is warning message')
    a.error('this is error message')
    a.fatal('this is fatal message, it is same as logger.critical')
    a.critical('this is critical message')

    service_name = "Booking"
    a.error('%s service is down!' % service_name)  # 使用python自带的字符串格式化，不推荐
    a.error('%s service is down!', service_name)  # 使用logger的格式化，推荐
    a.error('%s service is %s!', service_name, 'down')  # 多参数格式化
    a.error('{} service is {}'.format(service_name, 'down')) # 使用format函数，推荐


