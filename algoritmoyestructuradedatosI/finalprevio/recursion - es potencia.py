'''
ejercicio de recursión que
determina si un número entero es una potencia de otro número entero'''


def espotencia(base,n):
    if n == 1:
        return True
    elif n <1 or n % base != 0:
        return False
    else:
        return espotencia(base,n// base)