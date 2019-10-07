function[x] = Gauss_Seidel(A, b, n_iter, D, L, U)
	[row, col] = size(A);
	x = zeros(row, 1);
    for i = 1 : n_iter
        x = pinv(D + L) * (b - U * x);
    end
    