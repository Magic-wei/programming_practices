#! /usr/bin/env python3
# -*- coding: utf-8 -*-

## generator

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'None'

g = fib(6)

for n in g:
    print(n)

## Yanghui triangles

def triangles(max_n):
    n = 0;
    while(n<max_n):
        if n == 0:
            a = [1]
        elif n == 1:
            a = [1,1]
        else:
            temp = [a[j-1] + a[j] for j in range(1,n)]
            a = [1] + temp + [1]
        n += 1
        yield a

n = 0
results = []
for t in triangles(10):
    print(t)
    results.append(t)
    n = n + 1
    if n == 10:
        break
if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')
