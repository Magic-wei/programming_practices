%% Symbol Matrices Calculation
% Author: Wei Wang
% Date: 04/29/2019
% =======================================
clear;
%% Example #1

Matrix = sym('A',[3,4])
Matrix2 = sym('x_%d_%d', [4,3])

k = 10;
n = 3;
A = sym('A%d',[1,k])
x = sym('x%d',[1,k])
Al = sym('Al_%d_%d',k)
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

disp('Al = ')
disp(Al)

disp('Al^2 = ')
disp(Al^2)

disp('simplify(Al^2) = ')
disp(simplify(Al^2))

%% Example #2
% H = cell(k,k);
% for i = 1:k
% 	for j = 1:k
% 		if i == j
% 			H{i,j} = a;
% 		else if i < j
% 			H{i,j} = b;
% 		else if i > j
% 			H{i,j} = 1;
% 			for q = j:(i-1)
% 			    H{i,j} = H{i,j} * A(q);
%             end
%             end
%             end
% 		end
% 	end
% end

% disp('H = ')
% disp(H)

