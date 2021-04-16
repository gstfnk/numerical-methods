import numpy

math = numpy


def vectorLength(x1, x2):
    length = 0

    for i in range(0, len(x1)):
        length = length + pow((x1[i] - x2[i]), 2)

    output = math.sqrt(length)
    return output


def dominanceCriterion(A, b):
    n = len(b)
    ifConverge = True
    for i in range(0, n):
        sum = 0
        for j in range(0, n):
            sum = sum + math.abs(A[i][j])
        sum = sum - math.abs(A[i][i])
        if (A[i][i] < sum):
            ifConverge = False
    return ifConverge


def seidel(A, b, eps):
    n = len(b)

    # Dominance criterion - will the given method converge for the A matrix?
    ifConverge = dominanceCriterion(A, b)

    if (ifConverge == True):
        # One-dimensional matrix of length n, filled with 0
        xk = [0] * len(b)
        # One-dimensional matrix of length n, filled with 1
        xk1 = [1] * len(b)
        lengthXK = vectorLength(xk1, xk)
        while (lengthXK > eps):
            for i in range(0, n):
                xk[i] = xk1[i]
            for i in range(0, n):
                sum = 0
                for j in range(0, n):
                    if (i > j):
                        sum = sum + (A[i][j] * xk1[j])
                    if (i < j):
                        sum = sum + (A[i][j] * xk[j])
                xk1[i] = (1 / A[i][i]) * (b[i] - sum)
            lengthXK = vectorLength(xk1, xk)
        x = xk1
        print("Result:")
        return x
    else:
        print("The matrix does not meet the dominance criterion.")
    return


A = [[4, -1, -1, 0],
     [-1, 4, 0, -1],
     [-1, 0, 4, -1],
     [0, -1, -1, 4]]

b = [-1, 2, 0, 1]

print(dominanceCriterion(A, b))
print(seidel(A, b, 0.0001))
