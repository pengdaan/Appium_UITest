# -*- coding: utf-8 -*-
# @Time    : 2017/12/5 16:26
# @Author  : Leo_Peng
# @File    : Game.py
# @Software: PyCharm

#企业发放的奖金根据利润提成。
# 利润(I)低于或等于10万元时，奖金可提10%；
# 利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；
# 20万到40万之间时，高于20万元的部分，可提成5%；
# 40万到60万之间时高于40万元的部分，可提成3%；
# 60万到100万之间时，高于60万元的部分，可提成1.5%，高于100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？
def profit():
    profit=[100000,200000,4000000,6000000,10000000]
    result=0
    while result !=0000:
        b = int(input('请输入利润,输入0000退出系统：'))
        if b<=profit[0]:
            result=b+b*0.1
        if profit[0]<b and b<profit[1]:
            result=(b-profit[0])*0.75+profit[0]
        if  profit[1]<b and b<profit[2]:
            result=(b-profit[1])*0.05+profit[1]
        if  profit[2]<b and b<profit[3]:
            result=(b-profit[2])*0.03+profit[2]
        if  profit[3]<b and b<profit[4]:
            result=(b-profit[3])*0.15+profit[3]
        if  profit[4]<b :
            result=(b-profit[4])*0.01+profit[4]
        print(result)
    else:
        exit()


if __name__=='__main__':
    profit()
