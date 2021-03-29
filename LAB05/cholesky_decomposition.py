import numpy


def cholesky_decomposition(A):
    n = len(A)
    L = [0] * n
    Lt = [0] * n
    for i in range(0, n):
        L[i] = [0] * len(A[0])
        Lt[i] = [0] * len(A[0])
        for j in range(0, i + 1):
            sum = 0
            # sumination for diagonals:
            if (i == j):
                for k in range(0, j):
                    sum = sum + pow(L[i][k], 2)
                L[i][i] = numpy.sqrt(A[i][i] - sum)
            else:
                for k in range(0, j):
                    sum = sum + (L[i][k] * L[j][k])
                L[i][j] = (A[i][j] - sum) / L[j][j]
    for i in range(0, n):
        for j in range(0, n):
            Lt[i][j] = L[j][i]

    return L, Lt


#   Example from wikipedia:
A = [[4, 12, -16],
     [12, 37, -43],
     [-16, -43, 98]]

print(cholesky_decomposition(A))
