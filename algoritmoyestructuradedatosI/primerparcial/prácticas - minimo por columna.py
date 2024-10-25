"""Matriz mínimo de la suma de columnas"""
import random
def impresionmatriz(m):
    for f in m:
        for c in f:
            print("%3d" %c, end= " ")
        print()
    print()
    
def mindelasumadecolumnas(matriz):
    "Primero sumo cada columna"
    suma_columnas = [ ]
    for c in range(len(matriz[0])):
        suma = 0 #en cada columna sumaremos
        for f in range(len(matriz)):
            suma += matriz[f][c]
        suma_columnas.append(suma)
        print(f"Suma de columna {c + 1}: {suma}")  # Agregar impresión de la suma de cada columna
    "De la lista saco el min"
    minimo = min(suma_columnas)
    indice_minimo = suma_columnas.index(minimo)
    return minimo, indice_minimo
        

#programa principal
N = 4
matriz = [[random.randint(1,10) for c in range(N)] for f in range(N)]
impresionmatriz(matriz)
respuesta, pos = mindelasumadecolumnas(matriz)
print(f"El minimo de la suma de las columnas es : columna {pos} - {respuesta}. ")