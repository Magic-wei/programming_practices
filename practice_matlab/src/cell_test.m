%% Cell Calculation Test
% Author: Wei Wang
% Date: 04/29/2019
% =======================================

% cellfun is very useful
% usage: [A1,...,Am] = cellfun(func,C1,...,Cn,Name,Value)

%% Built-in function

% mean
C = {1:10, [2; 4; 6], []};
averages = cellfun(@mean, C)

% size
[nrows, ncols] = cellfun(@size, C)


% Create a cell array that contains character vectors, 
% and abbreviate each of them to their first three characters. 
% Because the output character vectors are nonscalar, 
% set UniformOutput to false.
days = {'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'};
abbrev = cellfun(@(x) x(1:3), days, 'UniformOutput', false)

% Calculate Covariance
c1 = rand(5,1);  c2 = rand(10,1);  c3 = rand(15,1);
d1 = rand(5,1);  d2 = rand(10,1);  d3 = rand(15,1);
C = {c1, c2, c3};
D = {d1, d2, d3};

covCD = cellfun(@cov, C, D, 'UniformOutput', false)

%% mat2cell
% get a 10x5 matrix with random integer from [0,50].
matrix = randi(50, 10, 5);
mc = mat2cell(matrix, [3 5 2], [3 2]) % columns -> 3|5|2, rows->3|2, 6 cells in total
sum_all = cellfun(@(x) sum(x(:)), mc)

% 

%% matrices calculation by sub-matrices
% M = [M_1 | M_2 | ... | M_n];
% W = [W_1 | W_2 | ... | W_n];
% return R = [M_1*W_1 | M_2*W_2 | ... | M_n*W_n];
% here just use tmp1 and tmp2 to replace every block.
n = 3;
m = 4;
tmp1 = randn(n);
tmp2 = randn(n,1);
M = repmat(tmp1,1,m);
W = repmat(tmp2,1,m);
blocks_M = reshape(M,n,n,[])
blocks_W = permute(W,[3 1 2])
R = reshape(sum(bsxfun(@times, blocks_M, blocks_W),2),n,[])

% given M = [A B C...] and a matrix D (all 2-dimensional). 
% D has dimensions x-by-x, and A, B, C, etc are each x-by-y. 
% return R = [D*A; D*B; D*C;...].
D = randn(n);
[size_m, size_n] = size(M);
result = zeros(size_m, size_n);
for ii=1:size_m:size_n
    result(:, ii:ii+size_m-1) = D * M(:, ii:ii+size_m-1);
end
disp('result = ')
disp(result)
clear result;

blksize = size(D, 1);
blkcnt = size(M, 2) / blksize;
blocks = mat2cell(M, blksize, repmat(blksize,1,blkcnt));
blocks = cellfun(@(x) D*x, blocks, 'UniformOutput', false);
result = cell2mat(blocks);
disp('result = ')
disp(result)