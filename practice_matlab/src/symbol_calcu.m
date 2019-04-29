%% Symbol Calculation
% Author: Wei Wang
% Date: 02/27/2019
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
R = sym(R);
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
