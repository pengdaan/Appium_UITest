# -*- coding: utf-8 -*-

# 加入体验计划，默认为选中
protocol = ('id,cn.wps.moffice_eng:id/collection_software_checkbox')

# 开始使用wps
using_wps = ('id,cn.wps.moffice_eng:id/first_start_ok')

# 手机或邮箱登陆
phone=('id,cn.wps.moffice_eng:id/home_roaming_login_with_email_and_password')

# QQ登录入口
qq = ('name,QQ登录')

# 微信登录入口
wechat = ('name,微信登录')

# 点击头像登录入口
Avatarlogin = ('id,cn.wps.moffice_eng:id/home_my_roaming_userinfo_pic')

# QQ账号输入框
qqUser = ('xpath,//android.widget.EditText[@content-desc=\"支持QQ号/邮箱/手机号登录\"]')

# QQ密码输入框
qqpwd = ('xpath,//android.webkit.WebView[@content-desc=\"QQ登录\"]/android.view.View[3]/android.widget.EditText[1]')

# QQ登录页面登录按钮
QQlogin = ('xpath,//android.view.View[@content-desc=\"登 录\"]')

#Table页：我的
Table_my = ('xpath,//android.widget.LinearLayout[@resource-id=\"cn.wps.moffice_eng:id/phone_home_toolbar_container\"]/android.widget.LinearLayout[4]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]/android.widget.ImageView[1]')

#我的页面下登录入口
mylogin=('id,cn.wps.moffice_eng:id/home_my_roaming_userinfo_pic')

#手机号码输入框
myphone=('id,cn.wps.moffice_eng:id/home_roaming_login_input_account')

#手机密码输入框
phonepwd=('id,cn.wps.moffice_eng:id/home_roaming_login_input_password')

#手机或邮箱页面登陆按钮
iplogin=('c,android.widget.Button')

#登录成功后断言元素
loginsucess=('id,cn.wps.moffice_eng:id/titlebar_back_icon')