"""Promedio por columna"""
import random

def impresion(m):
    for f in m:
        for c in f:
            print("%3d" %c, end="")
        print()
    print()
    

def promedioporcolumna(m):
    promedios = [ ]
    
    for c in range(len(m[0])):
        suma = 0
        promedio = 0
        for f in range(len(m)):
            suma += m[f][c]
        promedio = suma / len(m)
        promedios.append(promedio)
    return promedios
    
def impresiondepromedios(lista):
    for columna,promedio in enumerate(lista):
        print(f"Columna n°{columna} : promedio es de {promedio}")
    
    
#programa principal
N = int(input("Ingrese el tamaño de la matriz (NxN): "))
matriz = matiz = [[random.randint(1,10) for c in range(N)] for f in range(N)]
impresion(matriz)
listadepromedios = promedioporcolumna(matriz)
impresiondepromedios(listadepromedios)