# -*- coding: utf-8 -*-
import time
from Data.publicData import *
from PO.BasePage import Base

'''
app常用操作方法的封装
'''

class Wps(Base):

    def __init__(self,driver):
        '''
        继承父类初始化对象
        :param driver:
        '''
        Base.__init__(self,driver)


    def makeprotocol(self,status=True):
        '''
        app开始使用页面
        :param status:True为加入用户体验计划
        :return:
        '''
        if status:
            self.driver.clickButton(protocol)
            self.driver.clickButton(using_wps)
        else:
            self.driver.clickButton(using_wps)

    def Avatar(self):
        '''
        点击头像，进入登录页
        :return:
        '''
        self.driver.clickButton(Avatarlogin)


    def Table_my(self):
        '''
        进入个人中心页面，点击我的进入登录页
        :return:
        '''
        self.driver.clickButton(Table_my)
        self.driver.clickButton(mylogin)


    def qqlogin(self,user,pwd):
        '''
        使用QQ账号登录
        :return:
        '''
        self.driver.clickButton(qq)
        self.driver.send_keys(qqUser,user)
        self.driver.send_keys(qqpwd,pwd)
        self.driver.clickButton(QQlogin)


    def iplogin(self,user,pwd):
        '''
        使用手机号码登陆
        :return:
        '''
        self.driver.clickButton(phone)
        self.driver.send_keys(myphone,user)
        self.driver.send_keys(phonepwd,pwd)
        self.driver.clickButton(iplogin)









