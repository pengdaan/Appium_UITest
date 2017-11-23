# -*- coding: utf-8 -*-
# @Time    : 2017/11/23 10:51
# @Author  : Leo_Peng
# @File    : WpsLoginPage.py
# @Software: PyCharm

import time
from PO.BasePage import Base
import yaml,os
path=os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

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
        self.faile = open(path + '/Data/ElementData.ymal', 'r', encoding='utf-8')
        self.data = yaml.load(self.faile)
        self.faile.close()



    def makeprotocol(self,status=True):
        '''
        app开始使用页面
        :param status:True为加入用户体验计划
        :return:
        '''
        protocol = self.data['protocol']
        using_wps = self.data['using_wps']
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
        Avatarlogin = self.data['Avatarlogin']
        self.driver.clickButton(Avatarlogin)


    def Table_my(self):
        '''
        进入个人中心页面，点击我的进入登录页
        :return:
        '''
        Table_my = self.data['Table_my']
        mylogin = self.data['mylogin']
        self.driver.clickButton(Table_my)

        self.driver.clickButton(mylogin)


    def qqlogin(self,user,pwd):
        '''
        使用QQ账号登录
        :return:
        '''
        qq = self.data['qq']
        qqUser = self.data['qqUser']
        qqpwd = self.data['qqpwd']
        QQlogin = self.data['QQlogin']
        self.driver.clickButton(qq)
        self.driver.send_keys(qqUser,user)
        self.driver.send_keys(qqpwd,pwd)
        self.driver.clickButton(QQlogin)


    def iplogin(self,user,pwd,status):
        '''
        使用手机号码登陆
        :return:
        '''
        phone = self.data['phone']
        myphone = self.data['myphone']
        phonepwd = self.data['phonepwd']
        iplogin = self.data['iplogin']
        loginsucess = self.data['loginsucess']
        username = self.data['username']
        self.driver.clickButton(phone)
        self.driver.send_keys(myphone,user)
        self.driver.send_keys(phonepwd,pwd)
        self.driver.clickButton(iplogin)
        time.sleep(5)
        if status=='1':
            self.driver.clickButton(loginsucess)
            self.text_fail = self.driver.getText(username)
            return self.text_fail
        elif status=='2':
            print('逻辑未实现2')
            pass
        elif status=='3':
            print('逻辑未实现3')
            pass
        else:
            print('逻辑未实现4')
            pass










