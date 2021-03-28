def factorial(n):
    if n < 0:
        print("Factorial does not exist for negative numbers!")
    elif n == 0:
        print(1)
    else:
        result = 1;
        # Range generuje nam listę od 1 do number + 1
        for x in range(1, n + 1):
            result = result * x
        print(result)