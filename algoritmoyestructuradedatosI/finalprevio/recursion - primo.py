
'''un número es primo comprobando si es
divisible por algún número entre 2 y la raíz cuadrada del número. 
'''

def esprimo(n, divisor = 2):
    if n <= 1:
        return False
    elif divisor == n:
        return TrueS 
    elif n% divisor == 0:
        return False
    else:
        return esprimo(n, divisor +1)
    