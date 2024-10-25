"""LISTAS"""

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
    i +=1
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
#función
def imprimirlista(vec):
    largo = len(vec)
    for i in range(largo):
        print(vec[i], end=" ")
    print()
    
# programa principal
v = []
n = int(input("Ingresar un número o -1 para terminar  "))

while n!=-1: #lectura de datos
    v.append(n)
    n = int(input("Ingresar un número o -1 para terminar  "))
largo = len(v) #saber el largo de la lista = saber cuántos datos cargue.
if largo == 0:
    print("No se cargaron datos.")
else: # buscar el máximo de la lista
    mayor = v [0] # primera posición se guarda en mayor
    pos = 0
    for i in range(largo):
        if v[i]>mayor:
            mayor = v[i]
            pos = i
    imprimirlista(v)
    print("El máximo es", mayor, "y se encontró en la posición", pos)
    print("Borrando el", mayor)
    del v[pos]
    imprimirlista(v)
    
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