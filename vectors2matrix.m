function L = vectors2matrix(e, f)
    n = numel(e) + 1; % Determine the size of the resulting matrix
    L = zeros(n); % Initialize an n x n matrix with zeros

    % Fill the diagonal with ones
    L(1:n+1:end) = 1;

    % Fill the first lower diagonal with the vector e
    L(sub2ind([n, n], 2:n, 1:n-1)) = e;

    % Fill the second lower diagonal with the vector f
    L(sub2ind([n, n], 3:n, 1:n-2)) = f;
end