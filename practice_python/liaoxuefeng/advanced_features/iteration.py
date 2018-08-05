#! /usr/bin/env python3
# -*- coding: utf-8 -*-

## iteration
l = [1,2,4]
for num in l:
    print(num)

d = {'a': 1, 'b': 2, 'c': 3}
for k,v in d.items(): # don't understand where begin at 'c':3 
    print(k,v)

for k in d:
    print(k)

for v in d.values():
    print(v)
