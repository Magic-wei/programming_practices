#! /usr/bin/env python
# -*- coding = utf-8 -*-

from sympy import *

# Beautiful Printing
## [ref](http://certik.github.io/scipy-2013-tutorial/html/tutorial/printing.html#printers)

# init_session() is the same as the following 4 lines.

x, y, z, t = symbols('x y z t')
k, m, n = symbols('k m n', integer=True)
f, g, h = symbols('f g h', cls=Function)
init_printing()

formula = Integral(sqrt(1/x), x)

print('---- function: Integral(sqrt(1/x), x) ----')
print('string printer:', )
print(formula)
print('pretty printer:')
pprint(formula)
print('latex codes:')
pprint(latex(formula)) # the same as print(latex(formula))
print()

# basis
expr = x + y + 3
print('expr =', expr)
print('expr.subs(x, 3) =', expr.subs(x, 3))
print('expr.subs({x: t, y: 0.3}) =', expr.subs({x: t, y: 0.3}))
print('expr.subs([(x, t), (y, 0.3)]) =', expr.subs([(x, t), (y, 0.3)]))
print('pi.evalf() =', pi.evalf())
print('pi.evalf(10) =', pi.evalf(10))
print('expr.evalf(subs={x: 3}) =', expr.evalf(subs={x: 3}))
print('expr.evalf(subs={x: 3, y: t}) =', expr.evalf(subs={x: 3, y: t}))
print('expr.evalf(2, subs={x: 3, y: 2}) =', expr.evalf(2, subs={x: 3, y: 2}))
print()

a = (x+1)**2
b = x**2 + 2*x + 1
print('a is', a, 'and b is',b)
print('a == b?', a == b)
print('simplify(a-b) == 0?', simplify(a-b) == 0)
print('a.equals(b)?', a.equals(b))
print()

print('Note the difference between SymPy Integer type and Python int type')
print('Integer(1)/Integer(3) = ',Integer(1)/Integer(3))
print('1/3 = ',1/3)
print('x + 1/2 is', x + 1/2)
print('x + Rational(1, 2) can handle this issue:', x + Rational(1, 2))
print('x + S(1)/2 can also do this:', x + S(1)/2)
print()

print('S(1/3) =', S(1/3))
print('S("1/3") =', S('1/3'))
print()

print('Float(100) =', Float(100))
print('Float(100, 5) =', Float(100, 5))
print('Float(0.25, 4) =', Float(0.25, 4))
print("Float(100, '') =", Float(100, ''))
print("Float(12.34, '') =", Float('12.34', '')) # Float(12.34, '') returns error
print("S(0.25).n(10) =", S(0.25).n(10))
print("Float(0.1,10) + Float(0.1,3) =", Float(0.1,10) + Float(0.1,3))
print()

# variables
import sympy.abc as abc
print('sympy.abc has defined some symbols')
print(dir(abc))
print('abc.kappa + abc.pi =')
pprint(abc.kappa + abc.pi)
print('cos(pi/4) =', cos(pi/4))
print()

# simplification

# powsimp() applies identities 1 and 2 from above, from left to right.
print('powsimp function: default argument of combine=\'all\'')
print('example expression is x**n * x**m * y**n * y**m')
print("combine='all'",powsimp(x**n * x**m * y**n * y**m, combine='all'))
print("combine='exp'",powsimp(x**n * x**m * y**n * y**m, combine='exp'))
print("combine='base'",powsimp(x**n * x**m * y**n * y**m, combine='base'))
print()

# simplify() that attempts to apply all of these functions in an intelligent way 
# to arrive at the simplest form of an expression.
print('simplify(sin(x)**2 + cos(x)**2) =', simplify(sin(x)**2 + cos(x)**2))

# For polynomials, factor() is the opposite of expand()
print('expand((x + 1)**2) =', expand((x + 1)**2))
print('factor(x**2*z + 4*x*y*z + 4*y**2*z) =', factor(x**2*z + 4*x*y*z + 4*y**2*z))

# cancel() will take any rational function and put it into the standard canonical 
# form, p/q, where p and q are expanded polynomials with no common factors

print('cancel((x**2 + 2*x + 1)/(x**2 + x)) =', cancel((x**2 + 2*x + 1)/(x**2 + x)))
# apart() performs a partial fraction decomposition on a rational function.
print('apart((4*x**3 + 21*x**2 + 10*x + 12)/(x**4 + 5*x**3 + 5*x**2 + 4*x)) =', \
	apart((4*x**3 + 21*x**2 + 10*x + 12)/(x**4 + 5*x**3 + 5*x**2 + 4*x)))

# To simplify expressions using trigonometric identities, use trigsimp().
trigsimp(sin(x)**2 + cos(x)**2)
print()

# special functions

# factorial(n) represents n!=1⋅2⋯(n−1)⋅n and binomial(n, k) represents C_n^k.
print('factorial(n) =', factorial(n))
print('binomial(n, k) =', binomial(n, k))

# Example: Continued Fractions
def list_to_frac(l):
    expr = Integer(0)
    for i in reversed(l[1:]):
        expr += i
        expr = 1/expr
    return l[0] + expr
pprint(list_to_frac([x, y, z]))

# Calculus

# To take derivatives, use the diff() function. diff() can take multiple derivatives at once.
print("diff(exp(x**2), x) =", diff(exp(x**2), x))
print("diff(exp(x**2), x, 3) =", diff(exp(x**2), x, 3))
print("diff(exp(x**2), x, x, x) =", diff(exp(x**2), x, x, x))
print("diff(exp(x*y), x, y) =", diff(exp(x*y), x, y))
# To create an unevaluated derivative, use the Derivative class.
print("Derivative(exp(x*y), x, y) =")
pprint(Derivative(exp(x*y), x, y))
print("Derivative(exp(x*y), x, y).doit() =", Derivative(exp(x*y), x, y).doit())
print()

# To compute an integral, use the integrate function.
print("integrate(cos(x), x) =", integrate(cos(x), x))
print("integrate(exp(-x), (x, 0, oo)) =", integrate(exp(-x), (x, 0, oo)))
print("integrate(exp(-x**2 - y**2), (x, -oo, oo), (y, -oo, oo)) =", \
	integrate(exp(-x**2 - y**2), (x, -oo, oo), (y, -oo, oo)))
# If integrate is unable to compute an integral, it returns an unevaluated Integral object.
# As with Derivative, you can create an unevaluated integral using Integral.
print("Integral(cos(x), x) =")
pprint(Integral(cos(x), x))
print("Integral(cos(x), x).doit() =", Integral(cos(x), x).doit())
print("Integral(x**y*exp(-x), (x, 0, oo)) =")
pprint(Integral(x**y*exp(-x), (x, 0, oo)))
print()

# SymPy can compute symbolic limits with the limit function. lim_{x->x_0} f(x)
print("limit(sin(x)/x, x, 0) =", limit(sin(x)/x, x, 0))
print("(x**2/exp(x)).subs(x, oo) =", (x**2/exp(x)).subs(x, oo)) # oo means infinity.
print("limit(x**2/exp(x), x, 0) =", limit(x**2/exp(x), x, 0))
# Like Derivative and Integral, limit has an unevaluated counterpart, Limit.
print("Limit(x**2/exp(x), x, 0) =")
pprint(Limit(x**2/exp(x), x, 0))
print("Limit(x**2/exp(x), x, 0).doit() =", Limit(x**2/exp(x), x, 0).doit())
print()

# SymPy can compute asymptotic series expansions of functions around a point.
# To compute the expansion of 𝑓(x) around the point x=x0 terms of order xn, use f(x).series(x, x0, n).
print("(exp(x)).series(x, 0, 4) =", (exp(x)).series(x, 0, 4))
# If you do not want the order term, use the removeO method.
print("(exp(x)).series(x, 0, 4).removeO() =", (exp(x)).series(x, 0, 4).removeO())


# symbols
print("symbols('x:10') =", symbols('x:10'))
print("symbols('x5:10,y:5') =", symbols('x5:10,y:5'))
print("symbols('x:z') =", symbols('x:z'))
print("symbols('x(:c)') =", symbols('x(:c)'))
print("symbols('a:d, x:z') =", symbols('a:d, x:z'))
print("symbols('x:2(1:3)') =", symbols('x:2(1:3)'))
print("symbols('x\_:1\_:2') =", symbols('x\_:1\_:2'))
print("symbols('x(:1\,:2)') =", symbols('x(:1\,:2)'))
print()

# solvers
print("Eq(x, y) =", Eq(x, y))
print("solveset(x**2 - 1, x) =", solveset(x**2 - 1, x))
print("solveset(Eq(x**2, 1), x) =", solveset(Eq(x**2, 1), x))

print("solveset(sin(x) - 1, x, domain=S.Reals) =")
pprint(solveset(sin(x) - 1, x, domain=S.Reals))

print("solveset(sin(x) - 1, x, domain=S.Reals) =")
pprint(solveset(sin(x) - 1, x, domain=S.Reals))

diffeq = Eq(f(x).diff(x, x) - 2*f(x).diff(x) + f(x), sin(x))
print("dsolve: the solution f to Eq(f(x).diff(x, x) - 2*f(x).diff(x) + f(x), sin(x)) is")
pprint(dsolve(diffeq, f(x)))
print()

# Matrices
M = Matrix([[1,-1], [2,-3]])
N = Matrix([[0, 3], [0, 7]])
pprint(M)
print('M.shape:', M.shape) # return rows*cols
print('M.row(0) =')
pprint(M.row(0))
print('M.col(1) =')
pprint(M.col(1))
print('M*N + N*2 =')
pprint(M*N + N*2)
print('M**2 =')
pprint(M**2)
print('M**-1 =')
pprint(M**-1)
print('M.T =')
pprint(M.T)
print('eye(3) =')
pprint(eye(3))
print('zeros(2,3) =')
pprint(zeros(2,3))
print('diag(1,2,3) =')
pprint(diag(1,2,3))
print('diag(1, ones(2,2), Matrix([5,7,3])) =')
pprint(diag(1, ones(2,2), Matrix([5,7,3])))
print("M.det() =", M.det())

## Eigenvalues, Eigenvectors, and Diagonalization
M = Matrix([[3, -2,  4, -2], [5,  3, -3, -2], [5, -2,  2, -2], [5, -2, -3,  3]])
pprint(M)
print("M.eigenvals() =", M.eigenvals())
print("M.eigenvects() =")
pprint(M.eigenvects())
P, D = M.diagonalize()
print('M = PDP^-1 and P, D = M.diagonalize()')
print('P =')
pprint(P)
print('D =')
pprint(D)

# plotting
## [ref](https://docs.sympy.org/latest/modules/plotting.html)
from sympy.plotting import plot

p1 = plot(x**2, show=False)
p2 = plot(x, -x, show=False)
p1.extend(p2)
print(p1)
p1.show()
p3 = plot(x**3 + exp(x), (x, -5, 5)) # it will show directly without show=False

from sympy.plotting import plot_parametric
p4 = plot_parametric(cos(t), sin(t), (t, -5, 5))

# others
# source(simplify) # print the source code of a function
# help(pi) # use 'q' to quit help mode