def heron_algorithm(a, x):
    degree = len(a) - 1
    output = a[degree]
    while degree > 0:
        degree = degree - 1
        output = output * x + a[degree]
    return f"The result for the argument {x} is {output}"
