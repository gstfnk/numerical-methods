def LU_decomposition(A):
    L = [0] * len(A)
    U = [0] * len(A)
    for i in range(0, len(A)):
        L[i] = [0] * len(A[0])
        U[i] = [0] * len(A[0])
    for i in range(0, len(A)):
        L[i][i] = 1
        for k in range(0, len(A)):
            U[i][k] = A[i][k]
    for k in range(0, len(A)):
        for i in range(k + 1, len(A)):
            m = U[i][k] / U[k][k]
            L[i][k] = m
            for j in range(0, len(A)):
                U[i][j] = U[i][j] - (m * U[k][j])
    return U, L


A = [[3, 2, 3],
     [-9, -4, -6],
     [12, 12, 14]]

print(LU_decomposition(A))
