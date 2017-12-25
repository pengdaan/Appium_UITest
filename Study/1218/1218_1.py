# -*- coding: utf-8 -*-
# @Time    : 2017/12/18 10:12
# @Author  : Leo_Peng
# @File    : 1218_1.py
# @Software: PyCharm
x=set('abdce')
y=set('bdxyz')
print(x,y)
print('e' in x)
print(x-y) #获取y集合中不存在，x集合中存在的元素
print(x|y)#并集
print(x&y)#交集
print(set(x^y))#除去交集以外的所有元素
print(x>y,x<y)
z=x.intersection(y)
print(z)
z.add('SPAM')
print(z)
z.update(set(['X','Y']))
print(z)
z.remove('b')
print(z)
for item in set('abc'):
    print(item * 3)

S=set([1,2,3])
A=set('123')
print(S)
print(A)
print(S|set([3,4]))
print(S.union([3,4]))
print(S.intersection(set([1,3,5])))
print(S.issubset(range(-5,5)))


print(set([1,2,3,4]))
print(set('spam'))
S1={'s','p','a','m'}
S1.add('alot')
print(S1)
S2={1,2,3,4}
print(S2&{1,3})
print({1,5,6,3}|S2)
print(S2-{1,3,4})
print(S2>{1,3})#1,3存在于S2
S3=set()
S3.add(123)
print(S3)
print({1,2,3}|{4,5,6})
print({1,2,3}.issubset(range(-5,5)))
print({1,2,3}.issubset(range(-5,1)))
print({x**2 for x in[1,2,3,4]})
print({x for x in 'spam'})
L=[1,2,1,3,2,4,5]
print(set(L))
L=list(set(L))
print(L)
engineers={'bob','sue','ann','vic'}
managers={'tom','sue'}
print('bob'in engineers)
print(engineers&managers)
print(engineers.intersection(managers))
print(engineers|managers)
print(engineers.union(managers))
print(engineers - managers)
print(engineers.difference(managers))
print(engineers>managers)
print(engineers.issuperset(managers))
print({'bob','sue'}<engineers)
print({'bob','sue'}.issubset(engineers))
print((managers|engineers)>managers)
print(managers^engineers)
print((managers|engineers)-(managers^engineers))

