%% Tangent of Unit Circle
% Author: Wei Wang
% Date: 04/30/2019
% =======================================
close all; clear;
%% The first method
figure;
plot(sin(0:0.01:2*pi),cos(0:0.01:2*pi));
axis equal;
hold on;
n = 50;
theta = linspace(0,2*pi,n);
a = cos(theta);
b = sin(theta);
arrayfun(@(ii) fplot(@(x) -a(ii)/b(ii)*(x-a(ii))+b(ii),[-3,3]),1:n);
axis([-3,3,-3,3]);

%% The second method
figure;
R = 3;
plot(R*i*exp(i*(0:2*acos(1/R):200*R)))
axis equal
axis([-R,R,-R,R])