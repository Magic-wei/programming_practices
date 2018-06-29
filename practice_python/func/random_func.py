#! /usr/bin/env python3
# -*- coding: utf-8 -*-


# generic form, linear congruential generator(LCG): 
# x_i = (a*x_(i-1)+b) mod m
# u_i = x_i/m
# if a = 13, b = 0, m = 31:
# x_i = 13*x_(i-1) mod 31
# u_i = x_i / 31

u = []
x0 = 3
for i in range(60):
	x1 = 13*x0 %31
	u.append(x1/31)
	x0 = x1
	print(str(u[i]))

# 随机数的应用：
# 求平均值

