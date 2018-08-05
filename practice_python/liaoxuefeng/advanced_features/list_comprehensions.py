#! /usr/bin/env python3
# -*- coding: utf-8 -*-

## list comprehensions
a = list(range(1,11))
L=[]
for x in range(1,11):
    L.append(x*x)
print(L)

L1 = [x * x for x in range(1,11) if x % 2 == 0 ]
print(L1)

d = {'x': 'A', 'y': 'B', 'z': 'C'}
L2 = [k + '=' + v for k,v in d.items()]
print(L2)
L3 = [s.lower() for s in L2]
print(L3)

Lin = ['Hello', 'World', 18, 'Apple', None]
Lout1 = [s.lower() for s in Lin if isinstance(s,str)]
print(Lout1) # only print string

def lower_in_list(L):
    result = []
    for s in L:
        if isinstance(s,str):
            s = s.lower()
        result.append(s)
    return result
Lout2 = lower_in_list(Lin)
print(Lout2) # print all members in the list
