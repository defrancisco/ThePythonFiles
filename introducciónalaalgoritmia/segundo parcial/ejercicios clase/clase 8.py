# método de intercambio o burbujeo
def metodointercambio(v):
    desordenado = True
    while desordenado:
        desordenado = False
        for i in range (len(v)-1):
            if v[i]>v[i + 1]:
                aux = v[i]
                v[i] = v[i + 1]
                v[i + 1] = aux
                desordenado = True
                
# método de inserción
def metododeinsercion(v):
    for i in range(1, len(v)): # empieza del 2o elemento
        aux = v[i]
        j = i
    while j>0 and v[j-1]>aux:
        v[j] = v[j-1]
        j = j-1
    v[j] = aux
    
# 