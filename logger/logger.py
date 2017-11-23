# -*- coding: utf-8 -*-
# @Time    : 2017/11/23 10:32
# @Author  : Leo_Peng
# @File    : logger.py
# @Software: PyCharm

import logging,os,time
path=os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
class Logger():
    def __init__(self,title):
        self.day=time.strftime("%Y%m%d",time.localtime(time.time()))
        self.logger=logging.Logger(title)
        self.logger.setLevel(logging.INFO)
        self.loggerFile=logging.FileHandler(path + '/logger/log/%s.log'%self.day)
        self.loggerFile.setLevel(logging.INFO)
        self.control=logging.StreamHandler()
        self.control.setLevel(logging.INFO)
        self.formater=logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.loggerFile.setFormatter(self.formater)# 设置一个格式化器formatter
        self.control.setFormatter(self.formater)
        self.logger.addHandler(self.loggerFile) #为Logger实例增加一个处理器
        self.logger.addHandler(self.control)

    # 通过下面的方式进行简单配置输出方式与日志级别

    def debugInfo(self,message):
        self.logger.debug(message)

    def info_log(self,message):
        self.logger.info(message)

    def ware_log(self,message):
        self.logger.warning(message)

    def error_log(self,message):
        self.logger.error(message)
