def add_two_matrices(A, B):
    rows = len(A)
    columns = len(A[0])
    if rows != len(B):
        return "You cannot add matrices that have a different number of rows."
    elif columns != len(B[0]):
        return "You cannot add matrices that have a different number of columns."
    else:
        #   declaration of a nested list of variable lengths
        #   produce a list of rows size
        output = [0] * rows
        #   create a column for each row
        for i in range(len(A)):
            output[i] = [0] * len(A[0])
        #   final result
        for j in range(0, rows):
            for k in range(0, columns):
                output[j][k] = A[j][k] + B[j][k]
        return output