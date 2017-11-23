# -*- coding: utf-8 -*-
# @Time    : 2017/11/23 10:50
# @Author  : Leo_Peng
# @File    : BasePage.py
# @Software: PyCharm


import os
import time
from appium import webdriver
from PO.BasePage import Base
from selenium.webdriver.support.ui import WebDriverWait


class CommonDriver(object):
    """
    selenium的框架封装，封装后续测试过程中需要用到基础方法和代码
    """
    def __init__(self):

        driver = webdriver.Remote('http://localhost:4723/wd/hub', Base.AppSetting)
        try:
            self.driver = driver
        except Exception:
            raise NameError("driver Not Found!")


    def getElement(self, selector):
        """
        通过选择器定位元素
        :arg
        选择器应该以“i，xxx”的例子传递
        "x,//*[@id='langs']/button"
        :返回
        DOM元素
        """
        if ',' not in selector:
            return self.driver.find_element_by_id(selector)
        selector_by = selector.split(',')[0]    # 通过分割函数获取选择元素的方式
        selector_value = selector.split(',')[1] # 通过分割函数获取选择元素的元素值
        print(selector_value)
        if selector_by == "i" or selector_by == 'id':
            element=WebDriverWait(self.driver,5).until(lambda driver: self.driver.find_element_by_id(selector_value))
        elif selector_by == "n" or selector_by == 'name':
            element = WebDriverWait(self.driver,5).until(lambda driver: self.driver.find_element_by_name(selector_value))
        elif selector_by == "c" or selector_by == 'class_name':
            element = WebDriverWait(self.driver,5).until(lambda driver: self.driver.find_element_by_class_name(selector_value))
        elif selector_by == "l" or selector_by == 'link_text':
            element = WebDriverWait(self.driver,5).until(lambda driver: self.driver.find_element_by_link_text(selector_value))
        elif selector_by == "p" or selector_by == 'partial_link_text':
            element = WebDriverWait(self.driver,5).until(lambda driver: self.driver.find_element_by_partial_link_text(selector_value))
        elif selector_by == "t" or selector_by == 'tag_name':
            element = WebDriverWait(self.driver,5).until(lambda driver: self.driver.find_element_by_tag_name(selector_value))
        elif selector_by == "x" or selector_by == 'xpath':
            element = WebDriverWait(self.driver,5).until(lambda driver: self.driver.find_element_by_xpath(selector_value))
        elif selector_by == "s" or selector_by == 'selector_selector':
            element = WebDriverWait(self.driver,5).until(lambda driver: self.driver.find_element_by_css_selector(selector_value))
        else:
            #raise NameError("请输入有效类型的定位元素.")
            raise NameError("Please enter a valid type of targeting elements.")
        return element

    def getElements(self, selector):
        """
        通过选择器定位元素,获取一组数据
        :arg
        选择器应该以“i，xxx”的例子传递
        "x,//*[@id='langs']/button"
        :返回
        DOM元素
        """
        if ',' not in selector:
            return self.driver.find_elements_by_id(selector)
        selector_by = selector.split(',')[0]    # 通过分割函数获取选择元素的方式
        selector_value = selector.split(',')[1] # 通过分割函数获取选择元素的元素值

        if selector_by == "i" or selector_by == 'id':
            element = self.driver.find_elements_by_id(selector_value)
        elif selector_by == "n" or selector_by == 'name':
            element = self.driver.find_elements_by_name(selector_value)
        elif selector_by == "c" or selector_by == 'class_name':
            element = self.driver.find_elements_by_class_name(selector_value)
        elif selector_by == "l" or selector_by == 'link_text':
            element = self.driver.find_elements_by_link_text(selector_value)
        elif selector_by == "p" or selector_by == 'partial_link_text':
            element = self.driver.find_elements_by_partial_link_text(selector_value)
        elif selector_by == "t" or selector_by == 'tag_name':
            element = self.driver.find_elements_by_tag_name(selector_value)
        elif selector_by == "x" or selector_by == 'xpath':
            element = self.driver.find_elements_by_xpath(selector_value)
        elif selector_by == "s" or selector_by == 'selector_selector':
            element = self.driver.find_elements_by_css_selector(selector_value)
        else:
            #raise NameError("请输入有效类型的定位元素.")
            raise NameError("Please enter a valid type of targeting elements.")
        return element

    def click(self, selector):
        """
        It can click any text / image can be clicked
        Connection, check box, radio buttons, and even drop-down box etc..
        Usage:
        driver.click("i,el")
        """
        el = self.getElement(selector)
        el.click()

    def ElementFind(self,selector):
        '''
        判断元素是否存在
        :param selector:
        :return:
        '''
        try:
            el=self.getElement(selector)
            return el
        except:
            return False

    def send_keys(self,selector,value,clear_first=True,click_first=True):
        '''
        :param selector: [定位方式，定位元素]
        :param value: [输入的内容]
        :param clear_first: 不需要删除，直接输入
        :param click_first: 需要删除原来的内容，重新输入
        :return: None
        '''
        try:
            if click_first:
                self.getElement(selector).click()
            if clear_first:
                self.getElement(selector).clear()
            self.getElement(selector).send_keys(value)
        except AttributeError:
            print("%s 页面未能找到 %s 元素" %(self,selector))


    def getAttribute(self, selector, attribute):
        """
        获取元素属性的值.

        Usage:
        driver.get_attribute("i,el","type")
        """
        el = self.getElement(selector)
        return el.getAttribute(attribute)

    def getText(self, selector):
        """
        获取元素文本信息.
        Usage:
        driver.get_text("i,el")
        """
        el = self.getElement(selector)
        return el.text

    def getDisplay(self, selector):
        """
        获取要显示的元素，返回结果为true或false.
        Usage:
        driver.get_display("i,el")
        """
        el = self.getElement(selector)
        return el.is_displayed()

    def clickButton(self,selector):
        '''
        :param selector: [定位方式，定位元素]
        :return:
        '''
        try:
            self.getElement(selector).click()
        except AttributeError:
            print("%s 页面未能找到 %s 按钮" %(self,selector))

    def savePngName(self, name):
        """
        savePngName:生成图片的名称
        name：自定义图片的名称
        """
        day = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        fp = "Result\\" + day + "\\image\\" + day
        tm = self.saveTime()
        type = ".png"
        if os.path.exists(fp):
            filename = fp+"\\" + tm+"_"+name+type
            print (filename)
            #print "True"
            return filename
        else:
            os.makedirs(fp)
            filename = fp+"\\" + tm+"_"+name+type
            print (filename)
            #print "False"
            return filename


    def saveTime(self):
        """
        获取系统当前时间
        返回当前系统时间以括号中（2014-08-29-15_21_55）展示
        """
        return time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))


    def back(self):
        '''
        返回上一页
        :return:
        '''
        self.driver.back()

    def saveScreenshot(self,name):
        """
        saveScreenshot:通过图片名称，进行截图保存
        快照截图
        name:图片名称
        """
        #获取当前路径
        # #print os.getcwd()
        image = self.driver.save_screenshot(self.savePngName(name))
        return image

    def implicitlyWait(self, secs):
        """
        隐式等待页面上的所有元素.但是会导致app运行变慢
        Usage:
        driver.implicitly_wait(10)
        """
        self.driver.implicitly_wait(secs)


    # 获得机器屏幕大小x,y
    def getSize(self):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        return (x,y)

    # 屏幕向上滑动

    def swipeUp(self, t):
        l = self.getSize()
        x1 = int(l[0] * 0.5)  # x坐标
        y1 = int(l[1] * 0.75)  # 起始y坐标
        y2 = int(l[1] * 0.25)  # 终点y坐标
        self.driver.swipe(x1, y1, x1, y2, t)

    # 屏幕向下滑动

    def swipeDown(self, t):
        l = self.getSize()
        x1 = int(l[0] * 0.5)  # x坐标
        y1 = int(l[1] * 0.25)  # 起始y坐标
        y2 = int(l[1] * 0.75)  # 终点y坐标
        self.driver.swipe(x1, y1, x1, y2, t)

    # 屏幕向左滑动

    def swipLeft(self, t):
        l = self.getSize()
        x1 = int(l[0] * 0.75)
        y1 = int(l[1] * 0.5)
        x2 = int(l[0] * 0.05)
        self.driver.swipe(x1, y1, x2, y1, t)

    # 屏幕向右滑动
    def swipRight(self, t):
        l = self.getSize()
        x1 = int(l[0] * 0.05)
        y1 = int(l[1] * 0.5)
        x2 = int(l[0] * 0.75)
        self.driver.swipe(x1, y1, x2, y1, t)

    def ins(self,path):#安装app
        self.driver.install_app(path)

    def rem(self,baoming):#卸载app
        self.driver.remove_app(baoming)

    def rem_ios(self,bundleId):#ios
        self.driver.remove_app(bundleId)

    def close(self):#关闭app
        self.driver.close_app()

    def reset(self):#重置app
        self.driver.reset()

    def hide_keyb(self):#隐藏键盘
        self.driver.hide_keyboard()

    def launch_app(self):#启动app
        self.driver.launch_app()

    def quit(self):
        '''
        退出驱动
        :return:
        '''
        self.driver.quit()








