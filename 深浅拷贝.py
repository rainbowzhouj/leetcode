# -*- coding: utf-8 -*-
# @Time    : 2022/3/29 7:29 下午
# @Author  : rainbowzhouj
# @FileName: 深浅拷贝.py
# @Software: PyCharm

import copy
a=[1,2,3,4,['a','b']]
b=a
c=copy.copy(a)
d=copy.deepcopy(a)
a.append(5)
a[4].append('c')

print('a= ',a)
print('b= ',b)
print('c= ',c)
print('d= ',d)

a1 = {1: [1,2,3]}

b1 = a1.copy()
c1=a1[1].append(4)
print('a1= ',a1)
print('b1= ',b1)
print('c1= ',c1)