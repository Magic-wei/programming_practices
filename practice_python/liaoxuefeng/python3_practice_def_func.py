#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import math

def quadratic(a,b,c):
	str1 = '输入参数 a={:.1f}, b={:.1f}, c={:.1f}'.format(a,b,c)
	print(str1)
	temp=b**2-4*a*c
	if temp>0:
		x1 = (-b+math.sqrt(temp))/2/a
		x2 = (-b-math.sqrt(temp))/2/a
		print('二次方程有两个解，分别是 x1=%.2f, x2=%.2f' %(x1,x2))
		return x1,x2
	elif temp==0:
		x = -b / 2/a
		print('二次方程有一个解，它是 x=%.2f' %(x))
		return x
	else:
		print('二次方程没有实数解')
		return

quadratic(1,2,1)
quadratic(1,5,1)
quadratic(5,2,1)

# test:
print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')


def power(n,*args):
	num = len(args)
	if num<1:
		raise TypeError('input arguments number should be at least one!')
	results = []
	for i in args:
		temp = power1(i,n)
		results.append(temp)
		print(i)
	return results

def power1(x,n):
	return x**n

# test:

test_args=range(1,10)
print(test_args)
results = power(2,*test_args) # 输入一定要加上*号
print(results)
