def ordenamiento_burbuja_ascendente(diccionario):
    claves = list(diccionario.keys())
    n = len(claves)
    for i in range(n):
        for j in range(0, n-i-1):
            if claves[j] > claves[j+1]:
                claves[j], claves[j+1] = claves[j+1], claves[j]
    return claves

def ordenamiento_burbuja_descendente(diccionario):
    claves = list(diccionario.keys())
    n = len(claves)
    for i in range(n):
        for j in range(0, n-i-1):
            if claves[j] < claves[j+1]:
                claves[j], claves[j+1] = claves[j+1], claves[j]
    return claves

# Ejemplo de uso
mi_diccionario = {
    'manzana': 5,
    'banana': 2,
    'pera': 8,
    'uva': 3,
    'naranja': 6
}

claves_ascendente = ordenamiento_burbuja_ascendente(mi_diccionario)
claves_descendente = ordenamiento_burbuja_descendente(mi_diccionario)

print("Claves en orden ascendente:", claves_ascendente)
print("Claves en orden descendente:", claves_descendente)

