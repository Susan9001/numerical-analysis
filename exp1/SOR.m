function[x] = SOR(A, b, n_iter, D, L, U, w)
	[row, col] = size(A);
	x = zeros(row, 1);
    for i = 1 : n_iter
        x = pinv(w * L + D) * ((1-w) * D * x - w * U * x) + w * pinv(D + w * L) * b;
    end
