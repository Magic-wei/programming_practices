#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# 如果给定一个list或tuple，我们可以通过for循环来遍历这个list或tuple，这种遍历我们称为迭代（Iteration）。

## iteration
l = [1,2,4]
for num in l:
    print(num)

# 因为dict的存储不是按照list的方式顺序排列，所以，迭代出的结果顺序很可能不一样。
d = {'a': 1, 'b': 2, 'c': 3}
for k,v in d.items(): # the order of iteration differs very single execution, maybe a, b or c
    print(k,v)

for k in d:
    print(k)

for v in d.values():
    print(v)

# string can also be iterated
print('string can also be iterated:')
for ch in 'ABSFA':
    print(ch)

# we can see whether an object is iterable by collections module functions:
from collections import Iterable
print(isinstance('abec',Iterable))
print(isinstance([1,'a',4],Iterable))
print(isinstance(123,Iterable))

# we can also iterate mixed list or tuple:
for obj in [1,'ab', 2.0]:
    print(obj)
