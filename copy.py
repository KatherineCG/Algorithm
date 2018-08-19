# coding=utf-8
import copy
a = [1,2,3,4,['a', 'b']]

b = a
print a,b
print id(a),id(b)

c = copy.copy(a) #浅拷贝，不拷贝子对象，即['a','b']
d = copy.deepcopy(a) #深拷贝，拷贝子对象

a.append(5)
a[4].append('c')

print a
print b
print c
print d

print id(a)
print id(b)
print id(c)
print id(d)