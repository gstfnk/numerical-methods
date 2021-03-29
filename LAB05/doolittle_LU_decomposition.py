def doolittle_LU_decomposition(A):
    n = len(A)
    U = [0] * n
    L = [0] * n
    for i in range(0, n):
        U[i] = [0] * len(A[0])
        L[i] = [0] * len(A[0])
    for i in range(0, n):
        L[i][i] = 1
    for i in range(0, n):
        for k in range(i, n):
            sum = 0
            for j in range(0, i):
                sum = sum + (L[i][j] * U[j][k])
            U[i][k] = A[i][k] - sum
        for k in range(i, n):
            sum = 0
            for j in range(0, i):
                sum = sum + (L[k][j] * U[j][i])
            L[k][i] = int((A[k][i] - sum) / U[i][i])
    return U, L


A = [[2, -1, -2],
     [-4, 6, 3],
     [-4, -2, 8]]

print(doolittle_LU_decomposition(A))
