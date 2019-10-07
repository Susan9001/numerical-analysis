function[A, b, D, L, U] = init(n) 
    A = eye(n, n); % eye --∂‘Ω«œﬂæÿ’Û
    b = ones(n, 1);
    D = eye(n, n);
    L = eye(n, n);
    U = eye(n, n);

    for i = 1 : n
        A(i, i) = i;
        D(i, i) = i;
        L(i, i) = 0;
        U(i, i) = 0;
        if i < n
            A(i+1, i) = 0.5;
            A(i, i+1) = 0.5;
            L(i+1, i) = 0.5;
            U(i, i+1) = 0.5;
        end
        if i < (n - 1)
            A(i + 2, i) = 0.5;
            A(i, i + 2) = 0.5;
            L(i + 2, i) = 0.5;
            U(i, i + 2) = 0.5;
        end
    end