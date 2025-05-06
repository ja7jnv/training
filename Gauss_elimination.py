# Gauss elimination method to solve a system of linear equations

import numpy as np

def gauss_elimination(A, b):
    n = len(b)
    for i in range(n):
        # Find pivot row
        max_row = i
        for j in range(i+1, n):
            if abs(A[j, i]) > abs(A[max_row, i]):
                max_row = j
        # Swap rows in A and b
        A[[i, max_row], :] = A[[max_row, i], :]
        b[[i, max_row]] = b[[max_row, i]]
        # Elimination
        for j in range(i+1, n):
            factor = A[j, i] / A[i, i]
            A[j, i:] = A[j, i:] - factor * A[i, i:]
            b[j] = b[j] - factor * b[i]
    # Back substitution
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = (b[i] - np.dot(A[i, i+1:], x[i+1:])) / A[i, i]
    return x

# Example
A = np.array([[1, 2, 3], [1, 3, 3], [2, 5, 7]], dtype=float)
b = np.array([1, 2, 2], dtype=float)
x = gauss_elimination(A, b)

print(x)

