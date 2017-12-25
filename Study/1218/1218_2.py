# -*- coding: utf-8 -*-
# @Time    : 2017/12/18 16:50
# @Author  : Leo_Peng
# @File    : 1218_2.py
# @Software: PyCharm
x=set('spam')
y=set(['h','a','m'])
x.add((4,5))
x.update((4,5),'hello',[15,16,17,16],{'a':1,'b':2},{1,2,3,4})
print(x)
x.remove('s')
print(x)
print(len(x))
print('AA'in x)
s=set('hello')
print(s)
print(len(s))
print(x.issubset(y))