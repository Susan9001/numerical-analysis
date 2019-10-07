function[x] = Conjugate_Gradient(A, b, n_iter)
	[row, ~] = size(A);
	x = zeros(row, 1);
	d = b - A * x;
	r = d;
	zero = zeros(row, 1);

    for i = 1 : n_iter
		if r == zero
			break
		end
		a = (r' * r) / (d' * A * d);
		x = x + a * d;
        r_old = r;
		r = r - a * A * d;
		beta = (r' * r) / (r_old' * r_old);
		d = r + beta * d;
    end
