def heron_algorithm_lab(a, x, eps):
    test = 1000
    while test > eps:
        y = 0.5 * (x + a / x)
        test = abs(y - x)
        x = y
        print(x)
    return x
