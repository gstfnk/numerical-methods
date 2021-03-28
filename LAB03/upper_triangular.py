def upper_triangular(U, b):
    rowsB = len(b)
    x = [0] * rowsB
    x[rowsB - 1] = b[rowsB - 1] / U[rowsB - 1][rowsB - 1]
    for i in range(rowsB - 2, -1 , -1):
        suma = 0
        for j in range(rowsB - i - 2, rowsB):
            suma = suma + U[i][j] * x[j]
        x[i] = (b[i] - suma) / U[i][i]
    return x


#   Przykład z zadanie 1 z ćwiczeń
#   Macierz górna trójkątna
U = [[3, -4, 3],
     [0, 2, 3],
     [0, 0, -2]]
#   Macierz wynikowa
b = [23, 2, -4]

print(upper_triangular(U, b))
