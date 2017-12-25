# -*- coding: utf-8 -*-
# @Time    : 2017/12/4 17:15
# @Author  : Leo_Peng
# @File    : Game.py
# @Software: PyCharm


# 有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
for i in range(1,5):
    for j in  range(1,5):
        for k in range(1,5):
            if (i!=j)and(j!=k)and(i!=k):
                print(i,j,k)


import random

Number=[1,2,3,4,5,6,7,8,9]
nu=random.sample(Number,4)
print(nu)
a=input('nu:')
def num():
    b = []
    for i in a:
        b.append(i)
    for i in nu:
        if str(b[0]) == str(i) and str(b[0]) == str(nu[0]):
            print('%s 1A' % str(b[0]))
            result = 'A'

        if str(b[0]) == str(i) and str(b[0]) != str(nu[0]):
            print('%s 1B' % str(b[0]))
            result = 'B'

        if str(b[1]) == str(i) and str(b[1]) == str(nu[1]):
            print('%s 1A' % str(b[1]))
            result = 'A'

        if str(b[1]) == str(i) and str(b[1]) != str(nu[1]):
            print('%s 1B' % str(b[1]))
            result = 'B'

        if str(b[2]) == str(i) and str(b[2]) == str(nu[2]):
            print('%s 1A' % str(b[2]))
            result = 'A'

        if str(b[2]) == str(i) and str(b[2]) != str(nu[2]):
            print('%s 1B' % str(b[2]))
            result = 'B'

        if str(b[3]) == str(i) and str(b[3]) == str(nu[3]):
            print('%s 1A' % str(b[3]))
            result = 'A'

        if str(b[3]) == str(i) and str(b[3]) != str(nu[3]):
            print('%s 1B' % str(b[3]))
            result = 'B'



if __name__=='__main__':
    num()


# b=[]
# for i in a:
#     b.append(i)
# for i in nu:
#     if str(b[0])==str(i)and str(b[0])==str(nu[0]):
#        print('%s 1A'%str(b[0]))
#        result='1A'
#     if str(b[0]) == str(i) and str(b[0]) != str(nu[0]):
#         print('%s 1B' % str(b[0]))
#         result2 ='1B'
#     if str(b[1])==str(i)and str(b[1])==str(nu[1]):
#        print('%s 1A'%str(b[1]))
#        result = '1A'
#     if str(b[1]) == str(i) and str(b[1]) != str(nu[1]):
#         print('%s 1B' % str(b[1]))
#         result = '1B'
#     if str(b[2])==str(i)and str(b[2])==str(nu[2]):
#        print('%s 1A'%str(b[2]))
#        result = '1A'
#     if str(b[2]) == str(i) and str(b[2]) != str(nu[2]):
#         print('%s 1B' % str(b[2]))
#         result = '1B'
#     if str(b[3])==str(i)and str(b[3])==str(nu[3]):
#        print('%s 1A'%str(b[3]))
#        result = '1A'
#     if str(b[3]) == str(i) and str(b[3]) != str(nu[3]):
#         print('%s 1B' % str(b[3]))
#         result = '1B'




