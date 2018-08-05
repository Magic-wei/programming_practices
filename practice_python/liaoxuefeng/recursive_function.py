#! /usr/bin/env python3
# -*- coding: utf-8 -*-

#函数调用实现n>2个盘子如何实现汉诺塔
#汉诺塔规则：三个柱子A B C 起始位置A上有N个盘子，一次只能移动一个盘子，
# 盘子由小到大依次从上到下排列，移动盘子时仍然遵守上小下大的规则，打印如何实现将所有盘子从A移动到C上

def move(n,a,b,c):
	if n==1:
		print(a,'-->',c)
	else:
		move(n-1,a,c,b)
		move(1,a,b,c)
		move(n-1,b,a,c)

move(3, 'A', 'B', 'C')

