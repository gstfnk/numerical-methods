def gauss(A, b):
    for k in range(0, len(b)):
        for i in range(k + 1, len(b)):
            m = A[i][k] / A[k][k]
            b[i] = b[i] - (m * b[k])
            for j in range(0, len(b)):
                A[i][j] = A[i][j] - (m * A[k][j])
    return A, b



A = [[2, -3, -1],
     [-4, 10, 5],
     [8, -4, 4]]

b = [9, -29, 12]

print(gauss(A, b))