def horner_algorithm(a, c):
    b = [0] * (len(a) - 1)
    i = 0
    while (i < len(b)):
        if i == 0:
            b[i] = a[i]
        else:
            b[i] = b[i - 1] * c + a[i]
        i = i + 1
    return b