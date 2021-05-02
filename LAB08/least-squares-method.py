import numpy

def choleskyLt(A):
    n = len(A)
    L = [0] * n
    Lt = [0] * n
    for i in range(0, n):
        L[i] = [0] * len(A[0])
        Lt[i] = [0] * len(A[0])
        for j in range(0, i + 1):
            sum = 0
            if (i == j):
                for k in range(0, j):
                    sum = sum + pow(L[i][k], 2)
                L[i][i] = numpy.sqrt(abs(A[i][i] - sum))
            else:
                for k in range(0, j):
                    sum = sum + (L[i][k] * L[j][k])
                L[i][j] = (A[i][j] - sum) / L[j][j]
    for i in range(0, n):
        for j in range(0, n):
            Lt[i][j] = L[j][i]

    return Lt

def choleskyL(A):
    n = len(A)
    L = [0] * n

    for i in range(0, n):
        L[i] = [0] * len(A[0])

    for i in range(0, n):
        for j in range(0, i + 1):
            sum = 0
            # sumination for diagonals:
            if (i == j):
                for k in range(0, j):
                    sum = sum + pow(L[i][k], 2)
                L[i][i] = numpy.sqrt(abs(A[i][i] - sum))
            else:
                for k in range(0, j):
                    sum = sum + (L[i][k] * L[j][k])
                L[i][j] = (A[i][j] - sum) / L[j][j]

    return L


def lower_triangular(L, b):
    rowsB = len(b)
    x = [0] * rowsB
    x[0] = b[0] / L[0][0]
    for i in range(1, rowsB):
        suma = 0
        for j in range(0, i):
            suma = suma + L[i][j] * x[j]
        x[i] = (b[i] - suma) / L[i][i]
    return x


def upper_triangular(U, b):
    rowsB = len(b)
    x = [0] * rowsB
    x[rowsB - 1] = b[rowsB - 1] / U[rowsB - 1][rowsB - 1]
    for i in range(rowsB - 2, -1, -1):
        suma = 0
        for j in range(rowsB - i - 2, rowsB):
            suma = suma + U[i][j] * x[j]
        x[i] = (b[i] - suma) / U[i][i]
    return x


def leastSquaresMethod(x, y, n):
    # Cel 1
    dlugosc = n + 1
    Xsum = [0] * (2 * n)
    Ysum = [0] * dlugosc

    for i in range(1, (2 * n) + 1):
        tmp = 0
        for j in range(0, len(x)):
            tmp = tmp + (x[j] ** i)
        index = i - 1
        Xsum[index] = tmp

    for i in range(1, dlugosc + 1):
        tmp = 0
        for j in range(0, len(x)):
            tmp = tmp + ((x[j] ** (i - 1)) * y[j])
        index = i - 1
        Ysum[index] = tmp

    A = [0] * dlugosc
    for i in range(0, dlugosc):
        A[i] = [0] * dlugosc

    A[0][0] = len(x)

    for i in range(1, dlugosc):
        A[0][i] = Xsum[i - 1]

    for i in range(1, dlugosc):
        for j in range(0, dlugosc):
            A[i][j] = Xsum[i + j - 1]

    output = upper_triangular(choleskyLt(A),
                              lower_triangular(
                                           choleskyL(A), Ysum)
                              )

    return output


#   Example
x = [-1, 2, 5]
y = [5, -4, -13]
n = 1

print(leastSquaresMethod(x, y, n))
