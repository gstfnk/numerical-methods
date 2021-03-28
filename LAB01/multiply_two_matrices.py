def multiply_two_matrices(A, B):
    rowsA = len(A)
    rowsB = len(B)
    columnsA = len(A[0])
    columnsB = len(B[0])
    if rowsA == columnsB or rowsB == columnsA:
        #   declaration of a nested list of variable lengths
        #   produce a list of rows size
        output = [0] * rowsA
        #   create a column for each row
        for i in range(rowsA):
            output[i] = [0] * columnsB
        # multiply
        for i in range(rowsA):
            for j in range(columnsB):
                for k in range(rowsB):
                    output[i][j] += (A[i][k] * B[k][j])
        return output
    else:
        return "The number of columns in the first matrix must be equal to the number of rows in the second."
