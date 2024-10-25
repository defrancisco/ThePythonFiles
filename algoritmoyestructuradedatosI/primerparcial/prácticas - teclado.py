import random

def teclado():
    digitos = [1,2,3,4,5,6,7,8,9,0,"*","#"]
    mat = [ [0] * 3 for x in range(4)]
    random.shuffle(digitos)
    for f in range(len(mat)):
        for c in range(len(mat[0])):
             mat[f][c] = digitos[0]
             digitos.remove(mat[f][c])
    return mat

def impresion(m):
    for f in m:
        for c in f:
            print(f"{c}", end=" ")
        print()
    print()

#programa principal
matriz = teclado()
impresion(matriz)
    