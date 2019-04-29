%% Symbol Substitution
% Author: Wei Wang
% Date: 04/29/2019
% =======================================

%% Substitution

% Substitution in a Matrix Sense
syms x
f = x^3 - 15*x^2 - 24*x + 350;
A2 = magic(3)
b = sym2poly(f) % get the polynomial parameters
polyvalm(b,A) % get the value by replacing x in f with the matrix A
A^3 - 15*A^2 - 24*A + 350*eye(3)

syms a b c
A3 = [a b c; c a b; b c a]
alpha = sym('alpha');
beta = sym('beta');
A3(2,1) = beta;
A3 = subs(A,b,alpha)

syms a t
subs(exp(a*t) + 1, a, -magic(3))

A = sym('A', [2,2])
B = sym('B', [2,2])
A44 = subs(A, A(1,1), B)

% Multiple Substitutions
syms a b
subs(cos(a) + sin(b), [a, b], [sym('alpha'), 2])

% Multiple Scalar Expansion
syms x y
subs(x*y, {x, y}, {[0 1; -1 0], [1 -1; -2 1]})