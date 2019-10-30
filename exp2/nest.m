function y = nest(d, c, x, xi)
    % Compute value y of polynomial at x
    % d: array of d bas points
    if nargin < 4
        xi = zeroes(d, 1); 
    end
    y = c(d + 1);
    for i = d : -1 : 1
        y = y + c(i).* (x - b(i));
    end