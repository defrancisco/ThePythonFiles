# ejemplo 1 : escribir una función para simular el lanzamiento de un dado, utilizando número al azar.
import random #recordar importar y luego random
def lanzadordado( ):
    return random.randint(1, 6) #rand= random int= entero 
#programa principal
dado = lanzadordado( )
print(dado)

# ejemplo 2 : cargar una lista con números al azar entre 1 y 100, donde la cantidad de elementos será ingresada por el usuario.
  # Luego se solicita ingresar un valor y buscarlo en la lista, informando su ubicación o -1 si no se lo encuentra
import  random

def cargarlista(cantidad):
    lista = []
    for i in range(cantidad):
        lista.append(random.randint(1, 100))
    return lista

def imprimirlista(lista):
    for i  in range(len(lista)):
        print(lista[i], end=" ")
    print( )

def busquedasecuencial(lista, dato):
    i = 0
    while i <len(lista) and lista[i] != dato:
        i += 1
    if i < len(lista):
        return i
    else:
        return -1

# programa principal
cantidad = int(input("¿Cuántos elementos desea cargar?  "))
milista = cargarlista(cantidad)
imprimirlista(milista)
n = int(input("Ingrese el número a buscar  "))
pos = busquedasecuencial(milista, n)
if pos >=0:
    print("El elemento", n, "se encontró en la posición", pos)
else:
    print("El valor", n, "no se encontró en la lista")
    
#MÉTODO DE SELECCIÓN 
def metododeseleccion(v):
    largo = len(v)
    for i in range(largo - 1):
        for j in range(i+1, largo):
            if v[i] > v[j]:
                aux = v[i]
                v[i] = v[j]
                v[j] = aux
                
#BÚSQUEDA BINARIA
def busquedabinaria(v,dato):
    izq= 0
    der = len(v) - 1
    pos = -1
    while izq <= der and pos == -1:
        centro = (izq  + der ) //2
        if v[centro] == dato: 
            por = centro
        elif v[centro] < dato: #lado derecho
            izq = centro + 1 # cambio la variable de izquierda para que se vaya la derecha
        else: # lado izquierdo
            der = centro - 1 # variable derecha para que vaya  a la posición anterior, o sea, a la izquierda      
        return pos