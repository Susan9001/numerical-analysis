function [x] = Jacobi(A, b, n_iter, D, L, U)
	D_pinv = pinv(D);
	[row, col] = size(A);
	x = zeros(row, 1);
	for i = 1 : n_iter
		x = D_pinv * (b - (L + U) * x);
	end
    
