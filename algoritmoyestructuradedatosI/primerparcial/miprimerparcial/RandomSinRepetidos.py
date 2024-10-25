import random

def randomsinrepetidos1(minimo, maximo):
    """ Versión sin strings """
    if maximo<minimo:
        minimo, maximo = maximo, minimo  # Intercambio estilo Python
    hayrepetidos = True
    intentos = 0
    # Se establece un límite de 30 intentos para obtener un número al azar
    # sin dígitos repetidos. Esto evita ciclos infinitos en caso de ser imposible
    # obtener dicho número, por ejemplo si el intervalo fuera 440, 449.
    while hayrepetidos and intentos<30:
        n = random.randint(minimo, maximo)
        # Creamos una lista para contar los dígitos del 0 al 9
        digitos = [0] * 10
        candidato = n  # Hacemos una copia del n'umero antes de destruirlo
        # Descomponemos el número y contamos cuántas veces aparece cada dígito
        while n != 0:
            digito = n % 10
            n = n // 10
            digitos[digito] += 1
        # Si los 10 elementos de la lista son ceros y unos, ningún dígito está repetido y podemos salir
        if digitos.count(0)+digitos.count(1) == 10:
            hayrepetidos = False
        # Borramos la lista porque ya no es necesaria
        del digitos
        intentos+=1
    if hayrepetidos:
        return -1
    else:
        return candidato

def randomsinrepetidos2(minimo, maximo):
    """ Versión con strings """
    if maximo<minimo:
        minimo, maximo = maximo, minimo  # Intercambio estilo Python
    hayrepetidos = True
    intentos = 0
    # Se establece un límite de 30 intentos para obtener un número al azar
    # sin dígitos repetidos. Esto evita ciclos infinitos en caso de ser imposible
    # obtener dicho número, por ejemplo si el intervalo fuera 440, 449.
    while hayrepetidos and intentos<30:
        n = random.randint(minimo, maximo)
        cad = str(n)
        hayrepetidos = False
        # Verificamos si algún dígito se encuentra más de una vez
        for digito in cad:
            if cad.count(digito)>1:
                hayrepetidos = True
                break
        intentos+=1
    if hayrepetidos:
        return -1    # No se pudo obtener un número sin dígitos repetidos
    else:
        return n2

# Programa principal
a = int(input("Límite inferior? "))
b = int(input("Límite superior? "))
print()
num1 = randomsinrepetidos1(a, b)
print("Estrategia 1: El número al azar es", num1)
# num2 = randomsinrepetidos2(a, b)
# print("Estrategia 2: El número al azar es", num2)