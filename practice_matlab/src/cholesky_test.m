%% Cholesky Test
% Author: Wei Wang
% Date: 04/30/2019
% =======================================

clear;
% T = cholcov(SIGMA) computes T such that SIGMA = T'*T. SIGMA must be square, symmetric, 
% and positive semi-definite. If SIGMA is positive definite, then T is the square, upper 
% triangular Cholesky factor. If SIGMA is not positive definite, T is computed from an 
% eigenvalue decomposition of SIGMA.
% If use chol function, the matrix must be positive definite.
C1 = [3 1 1 2;1 2 1 2;1 1 2 2;2 2 2 3]
rank_C1 = rank(C1)
det_C1 = det(C1)
T = chol(C1)
C2 = T'*T

% You can use `gallery` function provides several symmetric, positive, definite matrices.

A=gallery('moler',5)
C=chol(A,'upper') % 'upper' (default) | 'lower'
isequal_1 = isequal(C'*C,A)

% pascal function have a nice structure for cholesky decomposition
n = 5;
X = pascal(n)
R = chol(X)

%% cov function - covariance
x = rand(1,10);
cov1 = cov(x) % for a vector, it returns scalar value

A = [5 0 3 7; 
     1 -5 7 3; 
     4 9 8 10];
cov2 = cov(A) % for a matrix, it returns covariance matrix, each column is a random variable and rows are observations.

