import random

def sumarentorno(mat, f,  c):
    tamaño = len(mat)
    suma = 0
    for i in range(f-1, f+2): # f-1 es el 1er valor del rango, f es el 2do y f+1 es el 3ro
        for j in range(c-1, c+2):
            if i>=0 and i<tamaño and j>=0 and j<tamaño:   # Si no nos excedimos de los bordes de la matriz...
                suma += mat[i][j]                         # ...sumamos el elemento
    suma -= mat[f][c]   # Restamos el elemento del centro, porque también fue sumado
    return suma

# def sumarencuadrados(mat,f,c):
#     tamaño = len(mat)
#     suma = 0
#     for i in range(f-1,f+2): #esto es f-1 | f | f+1
#         for j in range(c-1, c+2): #esto es c-1| c | c+1
#             if i>= 0 and i < tamaño and j >= 0 and j <tamaño: #no nos excedemos del rango
#                 suma += mat[i][j]
#     suma -= mat[f][c] # este es el del centro
#     return suma

def buscarmaximoentorno(mat):
    tamaño = len(mat)
    mayor = 0
    fmayor = 0
    cmayor = 0
    for f in range(tamaño):
        for c in range(tamaño):
            suma = sumarentorno(mat, f, c) #llamo la función así se la suma de cada una
            if suma>mayor:
                mayor = suma
                fmayor = f
                cmayor = c
    return fmayor, cmayor, mayor

# impresión----------
def imprimirmatriz(mat):
    for fila in mat:
        for col in fila:
            print(f"{col:3}", end="")
        print()

# Programa principal
n = int(input("Ingrese el tamaño de la matriz: "))
while n<3:
    print("Tamaño inválido. Debe ser mayor que 0")
    n = int(input("Ingrese el tamaño de la matriz: "))
# Creamos la matriz directamente con los números al azar usando listas por comprensión anidadas
matriz = [[random.randint(0, 100) for columna in range(n)] for fila in range(n)]
print()
imprimirmatriz(matriz)
print()
fila, col, maximo = buscarmaximoentorno(matriz) #desempaqueta los resultados
print(f"La manzana con mayor cantidad de vecinos está ubicada en fila {fila} y columna {col}, con {maximo} vecinos.")
