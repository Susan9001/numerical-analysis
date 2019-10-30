function y = nest(d, c, x, b)
    % Compute value y of polynomial at x
    if nargin < 4
       b = zeroes(d, 1); 
    end
    y = c(d + 1);
    for i = d : -1 : 1
        y = y.* (x - b(i)) + c(i);
    end