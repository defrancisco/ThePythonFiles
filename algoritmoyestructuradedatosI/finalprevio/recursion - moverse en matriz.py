def moverse_en_matriz(matriz, fila, columna):
    # Verificar si estamos dentro de los límites de la matriz
    if 0 <= fila < len(matriz) and 0 <= columna < len(matriz[0]):
        # Hacer algo con la celda actual, por ejemplo, imprimir su valor
        print("Visitando celda:", matriz[fila][columna])
        
        # Explorar todas las posibles direcciones de movimiento
        moverse_en_matriz(matriz, fila + 1, columna)  # Mover hacia abajo
        moverse_en_matriz(matriz, fila - 1, columna)  # Mover hacia arriba
        moverse_en_matriz(matriz, fila, columna + 1)  # Mover hacia la derecha
        moverse_en_matriz(matriz, fila, columna - 1)  # Mover hacia la izquierda

# Ejemplo de uso:
matriz_ejemplo = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Comenzar la exploración desde la celda (0, 0)
moverse_en_matriz(matriz_ejemplo, 0, 0)
