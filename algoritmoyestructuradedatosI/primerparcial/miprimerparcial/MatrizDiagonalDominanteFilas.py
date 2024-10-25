import random

def cargarmatriz(n):
    mat = [[0] * n for i in range(n)]
    for f in range(n):
        for c in range(n):
            mat[f][c] = random.randint(-100,100)
    return mat

def esdiagonaldominante(mat):
    # Hacemos una copia sin números negativos usando listas por comprensión anidadas.
    # La copia la hacemos para no alterar la matriz original.
    # Los números negativos se eliminan con la función abs().
    n = len(mat)
    copia = [[abs(mat[f][c]) for c in range(n)] for f in range(n)]
    esdiagdom = True
    for f in range(n):
        if copia[f][f]<= sum(copia[f])-copia[f][f]: #sumamos todo menos la diagonal
            esdiagdom = False
            break
    return esdiagdom

def imprimirmatriz(mat):
    print()
    for fila in mat:
        for elem in fila:
            print(f"{elem:4}", end="")
        print()
    print()

# Programa principal
n = int(input("Ingrese la dimensión de la matriz: "))
matriz = cargarmatriz(n)
imprimirmatriz(matriz)
if esdiagonaldominante(matriz):
    print("La matriz es diagonal dominante por filas")
else:
    print("La matriz NO es diagonal dominante por filas")