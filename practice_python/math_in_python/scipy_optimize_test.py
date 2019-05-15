#! /usr/bin/env python
# -*- coding = utf-8 -*-

'''
---------------------------------
 SciPy optimize Test
 Author: Wei Wang
 Date: 05/15/2019
---------------------------------
'''
import numpy as np
import scipy.optimize as sco
import matplotlib.pyplot as plt

# 1. minimize function
'''
 minimize f(x) = x1 * x2 + x1^2 + x3^2
 subject to: x1 = x2 * x3
             -5 < x2, x3 < 10
             x1 * (x2 + x3) < 10
'''

def cost_func(x):
	cost = x[0] * x[1] + x[0]**2 + x[2]**2
	return cost

## nonconstrained optimization
x0 = np.zeros([1,3])
result = sco.minimize(cost_func, x0, options={'disp': True})
print(result.x)

## constrained optimization

# variables constraints: lb < x < ub
var_bounds = sco.Bounds([-np.inf, -5, -5], [np.inf, 10, 10])

# equality and inequality constraints: c(x) == 0 or c(x) <= 0
cons = (
	{'type':'ineq', 'fun': lambda x: x[0]*(x[1]+x[2])-10},
    {'type':'eq', 'fun': lambda x: x[0]-x[1]-x[2]} )

options = {'disp': True, 'ftol': 1e-6}
result = sco.minimize(cost_func, x0, constraints=cons, options=options)
print(result.x)

# 2. curve fitting
def func(x, a, b, c):
	return a * np.exp(-b*x) + c

xdata = np.linspace(0, 4, 50)
y = func(xdata, 2.5, 1.3, 0.5)
np.random.seed(1729) # random number generator
y_noise = 0.2 * np.random.normal(size=xdata.size)
ydata = y + y_noise
plt.plot(xdata, ydata, 'b-', label='data')

## without constraints
popt, pcov = sco.curve_fit(func, xdata, ydata)
print('curve params fitting:', popt)
plt.plot(xdata, func(xdata, *popt), 'r-',label='fit: a=%.2f, b=%.2f, c=%.2f' % tuple(popt))

## with constraints: 0 <= a <= 3, 0 <= b <= 1 and 0 <= c <= 0.5
bounds = ([0., 0., 0.], [3., 1., 0.5]) # the same as (0., [3., 1., 0.5])
popt, pcov = sco.curve_fit(func, xdata, ydata, bounds=bounds)
plt.plot(xdata, func(xdata, *popt), 'g-', label='fit: a=%.2f, b=%.2f, c=%.2f' % tuple(popt))

# 3. least squares
'''
minimize F(x) = 0.5 * sum(rho(f_i(x)**2), i = 0, ..., m - 1)
subject to lb <= x <= ub

params:
  fun: f_i(x)
  loss: rho(s), there are some built-in loss function.
    - ‘linear’ (default) : rho(z) = z.
    - ‘soft_l1’ : rho(z) = 2 * ((1 + z)**0.5 - 1).
    - ‘huber’ : rho(z) = z if z <= 1 else 2*z**0.5 - 1.
    - ‘cauchy’ : rho(z) = ln(1 + z).
    - ‘arctan’ : rho(z) = arctan(z).
'''
def func_squared(params, x, y):
	return sum((func(x, *params) - y)**2)

def func_ls(params, x, y):
	return func(x, *params) - y

params0 = np.array([0., 0., 0.])
# res_ls = sco.least_squares(func_ls, params0, args=(xdata, ydata), loss='linear', f_scale=0.1)
res_sq = sco.least_squares(func_squared, params0, args=(xdata, ydata))
res_ls = sco.least_squares(func_ls, params0, args=(xdata, ydata))
res_ls_bounded = sco.least_squares(func_ls, params0, args=(xdata, ydata), bounds=bounds)
plt.plot(xdata, func(xdata, *(res_sq.x)), 'o:', label='least_squares using squared sum format')
plt.plot(xdata, func(xdata, *(res_ls.x)), 'm:', label='least_squares')
plt.plot(xdata, func(xdata, *(res_ls_bounded.x)), 'k--', label='least_squares bounded')

plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()

## linear least squares
'''
minimize 0.5 * ||A x - b||**2
subject to lb <= x <= ub
'''
from scipy.sparse import rand
np.random.seed(0)
m = 200
n = 100
A = rand(m, n, density=1e-2)
b = np.random.randn(m)
# print('A:', A)
# print('b', b)
lb = np.random.randn(n)
ub = lb + 1
res_linear_lsq = sco.lsq_linear(A, b, bounds=(lb, ub), lsmr_tol='auto', verbose=1)
print(res_linear_lsq.x)