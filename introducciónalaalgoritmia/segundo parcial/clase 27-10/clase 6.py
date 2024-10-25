"""CLASE NRO 6: Arreglos -Listas, Agregado y eliminación,
Subíndices, Búsqueda de max y min"""

#arreglo --- conjunto de variables agrupadas bajo un solo nombre
#subíndice --- posiciones de las variables. comienzan del 0
#print(vec[2]) constante / prin(vec[a] variable /print(vec[a] + 2) expresión
#end= " " dentro del print, sigue el renglón
# v. append(n) se agrega lo ingresado a la lista v = [ ]

# ejemplo 1 : Leer 100 números e imprimirlos en orden inverso
vec= [] #vacía ---> inicializar la lista para poder ingresar valores
i =  0 #variable
while i < 10:
    n = int(input("Ingrese un número "))
    vec.append(n) #lo guardamos con la variable n
    i = i + 1 #contador ordenar
# impresión
i = 9 #posición para imprimirlos en orden inverso
while i >=0:
    print(vec[i], end=" ") #al llegar al número cien empieza la impresión
    i = i - 1
-----------------------------------------------------------------------------------------------------------    
# ejemplo 2 : imprimir por pantalla una lista definida dentro del programa
lista = [ 2 , 3 , 4 , 5 , 7 , 4 , 9 , 7 , 9 ]
x = 0
while x<9: #número de cosas en lista
    print(lista[x], end=" ") # end es el espacio
    x = x + 1
    
-----------------------------------------------------------------------------------------------------------   
# ejemplo 3 : leer 50 num enteros, calcular su promedio e imprimir aquellos valores leídos sean mayores al promedio obtenido.

ELEMENTOS = 10 #variable constante que tiene valor determinado
v = []  # lista vacía
i = 0  # contador hasta tener 50 elementos
suma = 0 # acumulador. toda las cantidades ingresadas para obtener el promedio. no es variable constante suma valores cambiantes
while i < ELEMENTOS:
    n = int(input("Ingrese número  "))
    v.append(n)
    suma += n
    i +=1#recordar que el contador va en el mismo lugar que el return
promedio = suma/ELEMENTOS
print("El promedio es ", promedio)

# Segunda parte: Imprimir aquellos elementos leídos que sean mayores al promedio
i = 0
while i < ELEMENTOS: #mientras i sea menor que elementos. esta dentro de la cantidad requerida
    if v[i] > promedio: #preguntamos si la lista i es mayor que el promedio
        print(v[i]) #lo imprimimos
    i += 1 #actualizamos el contador
    
-----------------------------------------------------------------------------------------------------------  
# ejemplo 4 : Leer un conjunto de números y guardarlos en una lsita, finalizando la carga con -1. Luego buscar el mayor elemento eído, mostrarlo y eliminarlo del arreglo. Imprimir por pantalla la lsita antes y después del borrado.
def imprimirlista(v):
    largo = len(v)
    for i in range(largo):
        print(v[i], end= " ")
        
        
#programa principal
lista = [ ]
i = 0
n = int(input("Ingresar un nro o terminar con -1: "))
if n == -1: #rechazo que al principio pongan -1
    print("No se ingresaron valores")
else:# no fue -1 
    while n!= -1: #mientras que no sea menos uno
        lista.append(n)
        i += 1
        n = int(input("Ingresar un nro o terminar con -1: "))

mayor = lista[0]
pos = 0
largo = len(lista)
for i in range(largo):
    if lista[i] > mayor:
        mayor = lista[i]
        pos = i
    i += 1

print("Mi Lista")
imprimirlista(lista)
print( )
print("El mayor nro es",mayor,"en la posición", pos)
print("Eliminando el mayor....")
del lista[pos]
imprimirlista(lista)
    
-----------------------------------------------------------------------------------------------------------  
# ejemplo 5 : Escribir una función para ingresar números enteros en una lsita y devolverla como valor de retorno. La cantidad de valores a leer se recibe como parámetro.
# función
def cargarlista(cuantos):
    lista = [ ]
    for elemento in range(cuantos): #uno menos de cuantos porque cuantos es la cantidad de elementos que quiero que me carge en la lista
        n = int(input("Ingresa un número entero  "))
        lista.append(n) #vagones
    return lista

 # Programa principal
cant = int(input("Ingrese la cantidad de elementos: "))
print( )
milista = cargarlista(cant) 
print( )
print(milista)
-----------------------------------------------------------------------------------------------------------
# ejemplo 6 : Uso de for y range(). Imprimir los números del 1 al 100.
for numero in range(1, 101): # el valor final no esta incluido. siempre hacer uno más
    print(numero, end=" ")
-----------------------------------------------------------------------------------------------------------
# ejemplo 7 : Uso de range() con incremento. Imprimir los números impares del 1 al 100.
for impar in range (1, 101, 2): # el tercer parámetro actpua como incremento. soo dos parámetros el incremento es 1 a 1
    print(impar, end=" ")
-----------------------------------------------------------------------------------------------------------
# ejemplo 8 : Uso de range() con incremento negativo. Imprimir los números del 100 al 1.
for i in range(100, 0, -1): # cuando el incremento es negativo el valor inicial debe ser mayor que el valor final
    print(i, end= " ")