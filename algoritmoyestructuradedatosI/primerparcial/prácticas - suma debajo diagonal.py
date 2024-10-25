"""Desarrollar un programa que almacene números enteros obtenidos al azar entre 0 y 99 en una matriz de N x N y calcule la suma de los valores que se encuentran por debajo de la diagonal principal. El valor de N se ingresa por teclado. Imprimir la matriz obtenida y el resultado de la suma. Ejemplo para N = 5:
19   31   16   28   2
42   89   12    1   25
11  80   73   68   32
24   97    41    9    63
5     61    35    62    50

La suma de los elementos ubicados por debajo de la diagonal principal es 458
"""

import random

def impresionmatriz(m):
    for f in m:
        for c in f:
            print("%3d" %c, end=" ")
        print()
    print()
    

def sumadebajodiagonal(m):
    suma = [ ]
    for f in range(len(m)):
        for c in range(len(m[0])):
            if f > c:
                suma.append(m[f][c])
    
    suma_debajo_diagonal = sum(suma)
    return suma_debajo_diagonal,suma
    
#programa principal
N = 5
matriz = [[random.randint(0,99) for c in range(N)] for f in range(N)]
impresionmatriz(matriz)
respuesta, lista = sumadebajodiagonal(matriz)
print(f"La suma de los elementos ubicados por debajo de la diagonal principal es {respuesta}")
print()
print(f"Se utilizarons estos elementos para la suma: {lista}")