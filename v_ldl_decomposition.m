function [L, D] = v_ldl_decomposition(e, f)
   A = vectors2matrix(e, f)
    n = size(A, 1);
    L = zeros(n, n);
    D = eye(n);
    [L, D] = ldl_decomposition(A)
end