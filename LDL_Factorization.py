import numpy as np

def ldl_decomposition(A):
    n = A.shape[0]
    L = np.zeros((n, n))
    D = np.eye(n)
    
    for i in range(n):
        for j in range(i+1):
            if i == j:
                D[i, i] = A[i, i] - sum(L[i, k]**2 * D[k, k] for k in range(i))
            else:
                L[i, j] = (A[i, j] - sum(L[i, k] * L[j, k] * D[k, k] for k in range(j))) / D[j, j]
    
    np.fill_diagonal(L, 1)
    
    return L, D

# Example usage:
A = np.array([[4, 2, 2], [2, 5, 2], [2, 2, 6]])
L, D = ldl_decomposition(A)
print("L:\n", L)
print("D:\n", D)
print("LDL*:\n", L @ D @ L.T)
