def lagrange(x, xw, yw, n):
    n = n + 1
    output = [0] * len(x)
    for k in range(0, len(x)):
        for i in range(0, n):
            nom = yw[i]
            den = 1
            for j in range(0, n):
                if i != j:
                    nom = nom * (x[k] - xw[j])
                    den = den * (xw[i] - xw[j])
            output[k] = output[k] + (nom / den)

    return output


x = [6, 3]
xw = [-2, 1, 4]
yw = [5, 3, 7]
n = 2

print(lagrange(x, xw, yw, n))
