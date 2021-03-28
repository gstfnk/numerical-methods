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

#   Przykład z zadanie 1 z ćwiczeń
#   Macierz dolna trójkątna
L = [[-2, 0, 0],
     [1, 3, 0],
     [4, 2, 2]]
#   Macierz wynikowa
b = [2, 5, 2]

print(lower_triangular(L, b))
