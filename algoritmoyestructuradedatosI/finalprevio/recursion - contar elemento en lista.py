def contareleminlista(lista, elemento, indice = 0):
    if indice == len(lista):
        return 0
    elif lista[indice] == elemento:
        return 1 + contareleminlista(lista, elemento, indice+1)
    else:
        return contareleminlista(lista, elemento, indice+1)
        
        
        
        
lista = [1,2,2,34,5,7,2,6,7,9]        
print(contareleminlista(lista,2))      
        
        
        
        
        
        
