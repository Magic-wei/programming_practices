# /usr/bin/python3
# -*- code = utf-8 -*-

## map
def f(x):
    return x * x

r = map(f,list(range(1,10))) # map return a 'iterator' type value
print(list(r))

l_num2str = list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(l_num2str)

## reduce - Accumulation, need two params
from functools import reduce
def my_add(x,y):
    return x + y
print(reduce(my_add,list(range(1,10))))

def fn(x,y):
    return 10 * x + y
print(reduce(fn,list(range(1,10))))

def str2int(s):
    def fn(x, y):
        return x * 10 + y
    return reduce(fn, map(int, s))

number_str = '15968425565'
print(str2int(number_str))

a = '123'
b = list(map(int,a))
print(b)
