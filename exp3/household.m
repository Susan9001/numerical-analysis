function [Q, R, H] = household(A)
    [row, col] = size(A);
    H = zeros(row, row, col);
    x = A(:, 1);
    w = zeros(row, 1);
    w(1) = normest(x);
    v = w - x;
    P = (v * v')/(v' * v);
    H(:, :, 1) = eye(row, row) - 2 .* P;
    newA = H(:, :, 1) * A; % H1*A
    
    for i = 2:col
        [tmpR, tmpC] = size(newA);
        tmpX = newA(i:tmpR, i);
        tmpW = zeros(tmpR - i + 1, 1);
        tmpW(1) = normest(x);
        tmpV = tmpW - tmpX;
        tmpV
        tmpP = (tmpV * tmpV')./(tmpV' * tmpV);
        tmpH = eye(tmpR - i + 1, tmpR - i + 1) - 2 .* tmpP;
        H(:, :, i) = eye(row, row);
        H(i:row, i:row, i) = tmpH;
    end
    
    R = newA;
    Q = eye(row, row);
    for i = 1:col
        Q = Q * H(:, :, i);
    end
    
    
    
        
        
