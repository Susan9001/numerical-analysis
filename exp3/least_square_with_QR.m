function [x_res, RMSE] = least_square_with_QR(A, b, Q, R)
    [~, n] = size(A);
    d = (Q' * b);
    d = d(1:n, 1);
    x_res = inv(R(1:n, 1:n)) * d;
    r = b - A * x_res;
    RMSE = 0;
    for i = 1 : n
        RMSE = RMSE + r(i)^2;
    end
    RMSE = sqrt(RMSE);
    