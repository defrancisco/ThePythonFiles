"""
Aquí tienes uno que calcula la cantidad de veces que un número entero puede dividirse
por otro antes de llegar a 1, sin utilizar cadenas de caracteres:"""


def contardivisiones(n,divisor):
    if n < divisor:
        return 0
    else:
        #1 es el contador
        #n es dividido por el divisor
        #divisor es el mismo
        return  1 + contardivisiones(n // divisor, divisor)
    