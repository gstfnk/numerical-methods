def Stefaniak_Gabriela_gauss_jordan(A, b):
    rowsB = len(b)
    for k in range(0, rowsB):
        for i in range(k + 1, rowsB):
            m = A[i][k] / A[k][k]
            b[i] = b[i] - (m * b[k])
            for j in range(0, rowsB):
                A[i][j] = A[i][j] - (m * A[k][j])
    for i in range(rowsB - 1, -1, -1):
        for j in range(i - 1, -1, -1):
            m = A[j][i] / A[i][i]
            for k in range(i, len(A[0])):
                A[j][k] = A[j][k] - (m * A[i][k])
            b[j] = b[j] - m * b[i]
    x = [0] * rowsB
    for k in range(0,rowsB):
        x[k] = b[k]/A[k][k]
    output = ""
    for i in range(0,rowsB):
        output = output + " x" + str(i) + " = " + str(x[i]) + "\n"
    return output


#   Przykład z zadania 4 z ćwiczeń 3
A = [[2, -3, -1],
     [-4, 10, 5],
     [8, -4, 4]]
#   Macierz wyrazów wolnych
b = [9, -29, 12]

print(Stefaniak_Gabriela_gauss_jordan(A, b))
