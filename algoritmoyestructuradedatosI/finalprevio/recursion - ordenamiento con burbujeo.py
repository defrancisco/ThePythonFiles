
def burbujeo_recursivo(lista,n = len(lista)):
    #caso base: me queda un elemento en lista
    if n == 1:
        return
    #método de burbujeo
    else:
        for i in range(n-1):
            if lista[i] > lista[i+1]:
                temp = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = temp
        return burbujeo_recursivo(lista, n-1)
            