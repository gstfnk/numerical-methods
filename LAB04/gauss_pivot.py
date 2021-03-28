def gauss_pivot(A, b):
    for k in range(0, len(A) - 1):
        #   Tworzymy listę pivotów
        pivotList = [0] * len(A)
        for i in range(k, len(A)):
            #   Do listy pivotów wkładamy wartość bezwzgledną z elementów
            pivotList[i] = abs(A[i][k])
        indexPivotMax = pivotList.index(max(pivotList))
        #   Zamieniamy miejscami wiersze w A i w b
        A[indexPivotMax], A[k] = A[k], A[indexPivotMax]
        b[indexPivotMax], b[k] = b[k], b[indexPivotMax]
    #   Gauss:
    for k in range(0, len(b)):
        for i in range(k + 1, len(b)):
            m = A[i][k] / A[k][k]
            b[i] = b[i] - (m * b[k])
            for j in range(0, len(b)):
                A[i][j] = A[i][j] - (m * A[k][j])

    return A, b