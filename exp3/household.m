function [Q, R, H] = household(A)
    [m, n] = size(A);
    H = zeros(m, m, n);
    x = A(:, 1);
    w = zeros(m, 1);
    w(1, 1) = normest(x);
    v = w - x;
    P = (v * v')/(v' * v);
    H(:, :, 1) = eye(m) - 2 * P;   
    newA = H(:, :, 1) * A; % H1*A
    for i = 2:n
        tmpX = newA(i:m, i);
        tmpW = zeros(m - i + 1, 1);
        tmpW(1, 1) = normest(tmpX);
        tmpV = tmpW - tmpX;
        tmpP = (tmpV * tmpV')/(tmpV' * tmpV);
        H(:, :, i) = eye(m, m);
        H(i:m, i:m, i) = eye(m - i + 1, m - i + 1) - 2 * tmpP;
        newA = H(:, :, i) * newA;
    end

    R = A;
    for i = 1:n
        R = H(:, :, i) * R;
    end
    Q = H(:, :, 1);
    for i = 2:n
        Q = Q * H(:, :, i);
    end
    
    
    
        
        
