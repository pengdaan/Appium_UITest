# -*- coding: utf-8 -*-
# @Time    : 2017/12/22 10:27
# @Author  : Leo_Peng
# @File    : 1222_1.py
# @Software: PyCharm
import copy
L1=[1,2,3,4]
L2=L1
L3=L1[:] #切片
L4=copy.copy(L1) # 复制
L1[0]=21 ## 修改L1的值
print('打印L1,L2',L1,L2)
L3[1]=25 # 修改L3的值
print('打印L3',L3)
print('打印L4',L4)


S1={'KEY':'122'}
S2=S1
S1['KEY']='123'
print(S1,S2)

X=[42]
Y=copy.copy(X)
print(X==Y)
print(X is Y)