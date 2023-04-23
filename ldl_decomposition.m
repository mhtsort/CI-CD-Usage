function [L, D] = ldl_decomposition(A)
    n = size(A, 1);
    L = zeros(n, n);
    D = eye(n);

    for i = 1:n
        for j = 1:i
            if i == j
                D(i, i) = A(i, i) - sum(L(i, 1:i-1).^2 .* diag(D(1:i-1, 1:i-1))');
            else
                L(i, j) = (A(i, j) - sum(L(i, 1:j-1) .* L(j, 1:j-1) .* diag(D(1:j-1, 1:j-1))')) / D(j, j);
            end
        end
    end

    L(1:n+1:end) = 1; % Set the diagonal of L to 1
end


