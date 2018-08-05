#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# Practice 1: power() function

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

# test 1:
print('test 1 begins...')
test_args=range(1,10)
print(test_args)
results = power(2,*test_args) # 输入一定要加上*号
print(results)

# Practice 2: multi- operators

def product(*args):
	if len(args)==0:
		raise TypeError('args number should be at least one!!')
	s = 1
	for i in args:
		s = s * i
	return s

# test 2:
print('\ntest 2 begins...')
print('product(5) =', product(5))
print('product(5, 6) =', product(5, 6))
print('product(5, 6, 7) =', product(5, 6, 7))
print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))
if product(5) != 5:
    print('测试失败1!')
elif product(5, 6) != 30:
    print('测试失败2!')
elif product(5, 6, 7) != 210:
    print('测试失败3!')
elif product(5, 6, 7, 9) != 1890:
    print('测试失败4!')
else:
    try:
        product()
        print('测试失败5!')
    except TypeError:
        print('测试成功!')

# Practice 3: key words **kw

def student(name,age,*grade,city='beijing',education='graduate',**kw):
	print(name,'age=%d'%(age),'grade is',grade,'city is %s,education is %s'%(city,education),kw)

# test 3:
print('\ntest 3 begins...')
grade = [100,90,96.5]
student('wangwei',25,*grade,city='beijing',education='post graduate',hobby='piano')

