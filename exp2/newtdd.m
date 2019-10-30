function c = newtdd(x, y, n)
    % newtdd.m: output the coefficients of interpolating polynomial
    % compute Newton Triangle
    for j = 1:n 
        v(j,1) = y(j);
    end 
    for i = 2 : n % for column i
        for j = 1:n+1-i  	
            v(j,i) = (v(j+1,i-1)-v(j,i-1))/(x(j+i-1)-x(j));
        end 
    end
    % compute the coefficients  
    for i = 1:n 
        c(i) = v(1,i); % oead along top of triangle 
    end 