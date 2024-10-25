"""Escribir un programa para rellenar e imprimir una matriz de enteros de N x N con los números del 1 al 4,
respetando el patrón por cuadrantes detallado más abajo.
El programa debe servir para cualquier valor par de N, el que se ingresa por teclado. Ejemplo para N=6
mat = [ 1 1 1 2 2 2
            1 1 1 2 2 2
            1 1 1 2 2 2
            3 3 3 4 4 4
            3 3 3 4 4 4
            3 3 3 4 4 4
            ]
"""

def impresion(m):
    for f in m:
        for c in f:
            print("%3d" %c, end= " ")
        print()
    print()
    
def rellenoespecial(m):
    "Debo partir la matriz en cuatro secciones"
    mitad = len(m) // 2
    for f in range(len(m)):
        for c in range(len(m[0])):
            if f < mitad and c < mitad:
                m[f][c] = 1
            elif f  < mitad and c >= mitad:
                m[f][c] = 2
            elif f >= mitad and c < mitad:
                m[f][c] = 3
            else:
                m[f][c] = 4
    return m

def rellenoespecial(m):
    mitad = len(m) // 2
    for f in range(mitad):
        for c in range(mitad):
            # Primer cuadrante
            m[f][c] = 1
            # Segundo cuadrante
            m[f][c+mitad] = 2
            # Tercer cuadrante
            m[f+mitad][c] = 3
            # Cuarto cuadrante
            m[f+mitad][c+mitad] = 4
    return m

#programa principal
N = 6
if N % 2 != 0:
    print("N debe ser un número par.")
else:
    matriz = [[0]*N for x in range(N)]
    impresion(matriz)
    respuesta = rellenoespecial(matriz)
    impresion(respuesta)
