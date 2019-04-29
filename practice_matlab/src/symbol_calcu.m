%% Symbol Calculation
% Author: Wei Wang
% Date: 04/29/2019
% =======================================

n = 10;
% the first batch approach
c = [];
c = sym(c);
for k=1:n
   c(k)=['a',num2str(k)];
end
disp(c)

% the second batch approach
for k=1:n
	eval(['a' num2str(k) '=sym(''a' num2str(k) ''')']);
end

% the third batch approach
Matrix = sym('A',[3,4])
Matrix2 = sym('x_%d_%d', 4)

% matrix
A = sym('[a,b;c,d]');
A(1,2)

B = diag(c);
c1 = diag(B); % get the diagonal of B
c2 = diag(B,1); % get the sub-diagonal of B

% Kronecker product (克罗内克积)
H = kron(A,B);
disp(H)

W = [B;B];
disp(W)

Q = W'*H*W;
disp(Q)

I = eye(n);
R = [1,0,0;
     1,1,0;
     0,1,1];
R = sym(R)
M = kron(R,I);
disp(M)

len = size(R,1);
for k = 1:len
	r = ((k-1)*n+1):k*n;
	M(r,r) = B;
	if k < len
		r2 = (k*n+1):(k+1)*n;
		M(r2,r) = B;
	end
end
disp(M)

% repmat function
D = repmat(R,2,3);
disp(D)
S = repmat('What a wonderful day!',2,3);
disp(S)
N = repmat(NaN,2,3);
disp(N)

% transform to numerical calculation
a = 0; b = 0; c = 1; d = 0;
subs(A)
subs(B) % no error report if not given values of these variables

syms x
f = x^3 - 15*x^2 - 24*x + 350;
A1 = [1 2 3; 4 5 6];
subs(f,A1)

% transpose, det, rank
transpose(A)
det(A)
rank(A)
rank(subs(A))

% Create Symbolic Numbers
inaccurate1 = sym(1/1234567)
accurate1 = 1/sym(1234567)

inaccurate2 = sym(sqrt(1234567))
accurate2 = sqrt(sym(1234567))

inaccurate3 = sym(exp(pi))
accurate3 = exp(sym(pi))

% Create Large Symbolic Numbers
inaccurateNum = sym(11111111111111111111)
accurateNum = sym('11111111111111111111')
sym('1234567 + 1i')

% Create Symbolic Expressions from Function Handles
h_expr = @(x)(sin(x) + cos(x));
sym_expr = sym(h_expr)

h_matrix = @(x)(x*pascal(3));
sym_matrix = sym(h_matrix)

% Set Assumptions While Creating Variables
x = sym('x','real');
y = sym('y','positive');
z = sym('z','integer');
t = sym('t','rational');

assumptions % Check the assumptions on x, y, and z using assumptions.

assume([x y z t],'clear')
assumptions

% Set Assumptions on Matrix Elements
A = sym('A%d%d',[2 2],'positive')
assumptions(A)
assume(A,'clear');
assumptions(A)