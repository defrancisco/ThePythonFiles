def multiplosde7oterminanen7(n):
    lista = [x for x in range(1, n + 1) if x % 7 == 0 or x % 10 == 7]
    return lista

def sacardigitos(nro):
    suma = 0
    while nro != 0:
        suma += nro % 10  # Extraigo el último dígito y lo sumo
        nro //= 10  # Voy sacando los otros dígitos
    return suma

# Programa principal
N = int(input("Límite superior? "))
print("Lista con las características dadas")
lista = multiplosde7oterminanen7(N)
print(lista)
print()
print("Lista ordenada")
# Ordenar la lista utilizando como criterio de ordenamiento la suma de los dígitos de cada número
lista.sort(key=sacardigitos)
print(lista)
