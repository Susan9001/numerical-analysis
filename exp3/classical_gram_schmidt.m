function [Q, R] = classical_gram_schmidt(A)
    [row, col] = size(A);
    Q = zeros(row, col);
    R = zeros(col, col);
    
    for j = 1:col
        y = A(:, j);
        for i = 1:(j-1)
            R(i, j) = Q(:, i)' * A(:, j);
            y = y - Q(:, i) * R(i, j);
        end
        R(j, j) = normest(y);
        Q(:, j) = y / R(j, j);
    end
        
    