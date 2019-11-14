function [Q,R, H]= QRF_Householder_reflectors(A)
    [m,n] = size(A);
    x = A(:,1);
    w = zeros(m,1);
    H = ones(m,m,n);
    w(1,1) = normest(x);
    v = w-x;
    u = v/normest(v);
    H(:,:,1) = eye(m)-2*u*(u');
    tmp = H(:,:,1)*A;
    for i = 2:n
        x = tmp(i:m,i) ;
        w = zeros(m-i+1,1);
        w(1,1) = normest(x);
        v = w-x;
        u = v/normest(v);
        H(:,:,i) =eye(m,m);
        H(i:m,i:m,i) = eye(m-i+1)-2*u*(u');
        tmp = H(:,:,i)*tmp; 
    end
    R = A;
    for i=1:n
        R = H(:,:,i)*R;
    end
    Q = H(:,:,1);
    for i = 2:n
        Q = Q*H(:,:,i);
    end
    
    