%% Symbol Matrices Calculation
% Author: Wei Wang
% Date: 04/29/2019
% =======================================
clear all;
%% Example #1
Matrix = sym('A',[3,4])
Matrix2 = sym('x_%d_%d', [4,3])

k = 10;
n = 3;
A = sym('A%d',[1,k]);
x = sym('x%d',[1,k]);
Al = sym('Al_%d_%d',k);
a = sym('a');
b = sym('b');
for i = 1:k
	for j = 1:k
		if i == j
			Al(i,j) = a;
		else if i < j
			Al(i,j) = b;
		else if i > j
			Al(i,j) = 1;
			for q = j:(i-1)
			    Al(i,j) = Al(i,j) * A(q);
            end
            end
            end
		end
	end
end

% disp('Al = ')
% disp(Al)

% disp('Al^2 = ')
% disp(Al^2)

% disp('simplify(Al^2) = ')
% disp(simplify(Al^2))

%% Example #2
M = sym('M_%d_%d',k)
for i = 1:k
	for j = 1:k
		if i == j
			M(i,j) = 1;
		else if i < j || i > j + 1
			M(i,j) = 0;
		else if i == j + 1
			M(i,j) = A(j);
            end
            end
		end
	end
end

disp('M = ')
disp(M)

Q = sym('Q%d',[1,k])
W = sym('W_%d_%d',k)
for i = 1:k
	for j = 1:k
		if i == j
			W(i,j) = Q(i);
		else if i ~=j
			W(i,j) = 0;
            end
		end
	end
end

disp('M^T*W*M = ')
disp(M'*W*M)

L1 = sym('L%d',[1,k]);
L2 = sym('L_%d_%d',[k,k]);
L_mat = sym('L_%d_%d',k);
for i = 1:k
	for j = 1:k
		if i == j
			L_mat(i,j) = L1(i);
		else if i < j || i > j + 1
			L_mat(i,j) = 0;
		else if i == j + 1
			L_mat(i,j) = L2(i,j);
            end
            end
		end
	end
end

disp('L_mat = ')
disp(L_mat)

disp('L_mat*L_mat^T = ')
disp(L_mat*L_mat')