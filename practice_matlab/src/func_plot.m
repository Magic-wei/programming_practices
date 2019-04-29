%% Function Plot
% Author: Wei Wang
% Date: 04/29/2019
% =======================================
close all; clear;
%% Explicit Function Plot
figure;
syms x
f = x^3 - 6*x^2 + 11*x - 6;
fplot(f)
xlabel('x')
ylabel('y')
title(texlabel(f))
grid on

%% Implicit Function Plot
figure;
syms x y
eqn = (x^2 + y^2)^4 == (x^2 - y^2)^2;
fimplicit(eqn, [-1 1])

%% 3-D Plot
figure;
syms t
fplot3(t^2*sin(10*t), t^2*cos(10*t), t)

%% Create Surface Plot
figure;
syms x y
fsurf(x^2 + y^2)