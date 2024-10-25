def escuadradoperfecto(n,prueba = 1):
    if prueba * prueba == n:
        return True
    elif prueba * prueba > n:
        return False
    else:
        return escuadradoperfecto(n, prueba +1)