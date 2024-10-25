def sumalista(lista,indice= 0):
    "con len()"
    if indice == len(lista):
        return  0
    else:
        return lista[indice] + suma(lista,indice+1)
    
    
    
def sumalista(lista):
    "sin len()"
    #caso base: lista esta vacia 
    if not lista:
        return 0
    else:
    # Caso recursivo: retorna el primer elemento más la suma del resto de la lista
    #luego seguimos en la posicion siguiente por medio de rebanadas
        return lista[0] + sumalista(lista[1:])