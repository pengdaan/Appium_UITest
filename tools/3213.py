# -*- coding: utf-8 -*-
# @Time    : 2017/11/27 16:20
# @Author  : Leo_Peng
# @File    : 3213.py
# @Software: PyCharm

s = 'python'
print (s[::-1])

l = list(s)
l.reverse()
print (''.join(l))

e=[]
f=[]
d = {'x': 1, 'y': 2, 'z': 3}
for key in d:
    print(key)
    e.append(key)
print(e)
for key,value in d.items():
    print(value)
    f.append(value)
print(f)
