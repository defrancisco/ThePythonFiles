def sumaposicionimpares(lista, indice = 0):
    if indice >= len(lista):
        return 0
    elif indice % 2 != 0:
        return lista[indice] + sumaposicionimpares(lista,indice+1)
    else:
        return sumaposicionimpares(lista, indice +1)