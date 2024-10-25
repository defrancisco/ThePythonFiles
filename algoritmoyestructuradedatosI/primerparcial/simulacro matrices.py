"""Un cuadrado mágico es una matriz cuadrada de números enteros en el que la suma de sus elementos en cada fila, columna o diagonal arroja el mismo resultado. Este valor es conocido como "suma mágica". Ejemplo:
4 3 8
9 5 1
2 7 6

Cuadrado mágico con suma 15:
4+3+8 = 9+5+1 = 2+7+6 = 15 (filas)
4+9+2 = 3+5+7 = 8+1+6 =15 (columnas)
4+5+6 = 2+5+8 = 15 (diagonales)

Escribir un programa para cargar valores en una matriz de N x N (con N ingresado por el usuario) e imprimir un mensaje indicando si se trata de un cuadrado mágico o no. Si lo es, mostrar su suma mágica. Imprimir también la matriz utilizada.
"""
import random

def imprimirmatriz(mat):
    for f in mat:
        for c in f:
            print("%3d" %c, end=" ")
        print()
    print()
    
def escuadradomagico(mat):
    esmagico = True # control
    filas = len(mat)
    columnas = len(mat[0])
    
    #entro a cada fila y hago su sumatoria
    #entro el resultado en una lista
    suma_filas = [ ]
    for fila in mat:
        suma_filas.append(sum(filas))
    #control
    if min(suma_filas) != max(suma_filas):
        esmagico = False
        
    #recorro cada columna y hago su sumatoria
    #entro el resultado en una lista
    suma_columnas = [ ]
    for c in range(columnas):
        suma = 0
        for f in range(filas):
            suma += matriz[f][c]
        suma_columnas.append(suma)
    #control
    if min(suma_columnas) != max(suma_columnas):
        esmagico = False
        
    #diagonales
    principal = 0
    secundaria = 0
    for f in range(filas):
        principal += mat[f][f]
        secundaria += mat[f][filas-c+1]
    if principal != secundaria:
        esmagico = False
    return esmagico
    
    
            
#programa principal
N = int(Input("Ingrese el tamaño de la matriz: "))
matriz = [[random.randint(0,9) for c in range(N)] for f in range(N) ]
"""
mat = [ [4,3,8],
        [9,5,1],
        [2,7,6] ]
"""
imprimirmatriz(mat)
if escuadradomagico(mat):
    print("Es un cuadrado mágico")
else:
    print("No es un cuadrado mágico")