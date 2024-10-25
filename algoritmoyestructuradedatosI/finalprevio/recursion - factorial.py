def factorial(n):
    #caso base
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
#N * N-1
#ejemplo

print(factorial(4))

