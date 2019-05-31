#! /usr/bin/env python
# -*- coding = utf-8 -*-

'''
---------------------------------
 CVXPY Optimization Test
 Author: Wei Wang
 Date: 05/31/2019
---------------------------------
'''

import cvxpy as cp
import numpy as np
import matplotlib.pyplot as plt

'''
ref: 
[basis](https://www.cvxpy.org/tutorial/intro/index.html)
[advanced](https://www.cvxpy.org/tutorial/advanced/index.html)
'''

# Create scalar optimization variables
x = cp.Variable()
y = cp.Variable()

# Create two constraints
constraints = [x + y == 1,
               x - y >= 1]

# Form objective
obj = cp.Minimize((x - y)**2)

# Form and solve problem
prob = cp.Problem(obj, constraints)
prob.solve() # return the optimal value
print("status (prob):", prob.status)
print("optimal value:", prob.value) # optimal obj
print("optimal var:", x.value, y.value) # optimal variables

# Changing the problem

# replace the objective
prob2 = cp.Problem(cp.Maximize(x+y), prob.constraints)
prob2.solve()
print("status (prob2):", prob2.status)
print("optimal value:", prob2.value) # optimal obj
print("optimal var:", x.value, y.value) # optimal variables

# replace the constraint (x + y == 1)
constraints = [x + y <= 3] + prob.constraints[1:]
prob3 = cp.Problem(prob2.objective, constraints)
prob3.solve()
print("status (prob3):", prob3.status)
print("optimal value:", prob3.value) # optimal obj
print("optimal var:", x.value, y.value) # optimal variables

# infeasible problem
prob4 = cp.Problem(cp.Minimize(x), [x>=1, x<=0])
prob4.solve()
print("status (prob4):", prob4.status)
print("optimal value:", prob4.value) # optimal obj
print("optimal var:", x.value) # optimal variables

# unbounded problem
prob5 = cp.Problem(cp.Maximize(x))
prob5.solve()
print("status (prob5):", prob5.status)
print("optimal value:", prob5.value) # optimal obj
print("optimal var:", x.value) # optimal variables

'''
Note:
If the solver completely fails to solve the problem, 
CVXPY throws a SolverError exception. 
If this happens you should try using other solvers.
See the discussion of 

[Choosing a solver](https://www.cvxpy.org/tutorial/advanced/index.html#solvers)

for details.
'''

# Solve with ECOS Solver.
prob.solve(solver=cp.ECOS)
print("status (prob with ECOS Solver):", prob.status)
print("optimal value:", prob.value)
print("optimal var:", x.value, y.value)

'''
Vectors and matrices
'''

# scalar variable
a = cp.Variable()

# vector variable with shape(5,)
x = cp.Variable(5)

# matrix variable with shape (5,1)
x = cp.Variable((5,1))

# matrix variable with shape (4, 7)
A = cp.Variable((4,7))

# solves a bounded least-squares problem
m = 10
n = 5
np.random.seed(1)
A = np.random.randn(m,n)
b = np.random.randn(m)
x = cp.Variable(n)
obj = cp.Minimize(cp.sum_squares(A*x-b))
constraints = [0 <= x, x <= 1] # elementwise, each entry of x is constrained
prob = cp.Problem(obj, constraints)
print("status (least-squares prob):", prob.status)
print("optimal value:", prob.value)
print("optimal var:", x.value)

# advanced setting on constraints and variables

# constrain a matrix to be positive or negative semidefinite
M = cp.Variable((5,5))
constr1 = (M >> 0) # positive
constr2 = (M << 0) # negative
consrt = (M == M.T) # symmetric

'''
Parameters
'''

# positive scalar parameter
m = cp.Parameter(nonneg=True)

# column vector parameter with unknown sign (default)
c = cp.Parameter(5)

# matrix parameter with negative entries
G = cp.Parameter((4,7), nonpos=True) # nonpos = non positive

# assigns a constant value to G
G.value = -np.ones((4, 7))

# create scalar parameter, then assign value
rho = cp.Parameter(nonneg=True)
rho.value = 2

# Initialize parameter with a value
rhp = cp.Parameter(nonneg=True, value=2)

# a more complex problem
n = 15
m = 10
np.random.seed(1)
A = np.random.randn(n, m)
b = np.random.randn(n)
gamma = cp.Parameter(nonneg=True)

x = cp.Variable(m)
error = cp.sum_squares(A*x-b)
obj = cp.Minimize(error + gamma * cp.norm(x, 1))
prob = cp.Problem(obj)

# Construct a trade-off curve of ||Ax-b||^2 vs. ||x||_1
sq_penalty = []
l1_penalty = []
x_values = []
gamma_vals = np.logspace(-4, 6)
for val in gamma_vals:
    gamma.value = val
    prob.solve()
    # Use expr.value to get the numerical value of
    # an expression in the problem.
    sq_penalty.append(error.value)
    l1_penalty.append(cp.norm(x, 1).value)
    x_values.append(x.value)

plt.rc('text', usetex=True)
plt.rc('font', family='serif')
plt.figure(figsize=(6,10))

# Plot trade-off curve.
plt.subplot(211)
plt.plot(l1_penalty, sq_penalty)
plt.xlabel('$\|x\|_1$', fontsize=16)
plt.ylabel('$\|Ax-b\|^2$', fontsize=16)
plt.title('Trade-Off Curve for LASSO', fontsize=16)

# Plot entries of x vs. gamma.
plt.subplot(212)
for i in range(m):
    plt.plot(gamma_vals, [xi[i] for xi in x_values])
plt.xlabel('$\gamma$', fontsize=16)
plt.ylabel('$x_{i}$', fontsize=16)
plt.xscale('log')
plt.title('Entries of $x$ vs. $\gamma$', fontsize=16)

# plt.tight_layout()
# plt.show() # uncomment these two lines to show plotting

'''
fast parallel computation
'''

from multiprocessing import Pool
# Assign a value to gamma and find the optimal x.
def get_x(gamma_value):
    gamma.value = gamma_value
    result = prob.solve()
    return x.value

# Parallel computation (set to 1 process here).
print(len(x_values))
pool = Pool(processes = 1)
x_values = pool.map(get_x, gamma_vals)
print(len(x_values))