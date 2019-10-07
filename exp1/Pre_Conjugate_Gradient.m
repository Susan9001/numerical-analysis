function[x] = Pre_Conjugate_Gradient(A, b, n_iter, M)
	[row, ~] = size(A);
	x = zeros(row, 1);
	r = b - A * x;
    d = pinv(M) * r;
    z = d;
	zero = zeros(row, 1);

    for i = 1 : n_iter
		if r == zero
			break
		end
		a = (r' * z) / (d' * A * d);
		x = x + a * d;
		r_old = r;
		r = r - a * A * d;
		z_old = z;
		z = pinv(M) * r;
		beta = (r' * z) / (r_old' * z_old);
		d = z + beta * d;
    end
