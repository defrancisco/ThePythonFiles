def cargarlista(min, max):
    print("Los nros a ingresar deben estar entre", min, "y", max)
    a = int(input("Ingrese un nro o el -1 para terminar  "))
    if a == -1: #verificar que no este vacía
        print("No se ingresaron valores")
    else:
        while a!= -1:
            if a<min or a>max: #afuera de los parámetros
                print("Error. Ingresa nro entre", min, "y", max)
                a = int(input("Ingrese un nro o el -1 para terminar  "))#pedimos de vuelta nros válidos
            else: #en orden
                v.append(a) #agregamos agones al tren. hay que guardar los nros
                a = int(input("Ingrese un nro o el -1 para terminar  ")) #pedimos de vuelta otro vagon
    return v #return delcaración de lista

def capicua(lista): #ejercicio 3
    largo = len(lista)
    lista2 = [ ]
    for i in range (largo-1,-1,-1): #al revés
        lista2.append(lista[i])
    
    print("Ejercicio 3")
    print(lista)
    print(lista2)
    if lista == lista2:
        print("Las listas son capicúa.")
    else:
        print("Las listas no son capicúas")

def buscardato(lista,dato): #busqueda secuencial. no esta ordenada la lista
    i = 0 #subíndice
    contador = 0
    while i <len(lista):
        if lista[i] == dato:
            contador += 1
        i += 1
    return contador

def imprimiralrevés(lista): #ejercicio 5
    largo = len(lista)
    for i in range(largo-1, -1, -1):
        print(lista[i], end=" " )
    print()
    
def busquedasecuencial(lista,dato):
    pos = -1
    i = 0
    while i< len(lista):
        if lista[i] == dato:
            pos = i
            print("El dato", dato,"se encontró en la pos", pos)
        i += 1 #saber si hay más = contador
        
    if pos == -1:
            print("No se encontro el dato en ninguna posición.")
    
    
    
#programa principal
v = [ ]
#ejercicio 1
x = int(input("Ingresar prámetro minimo "))
y = int(input("Ingresar prámetro máximo "))
milista = cargarlista(x,y)
print()
print("Ejercicio 1")
print(milista)
print("----------------")

#ejercicio 2. sumar, cantidad, porcentaje y promedio
i = 0
suma = 0
contador = 0
for i in range(len(milista)):
               suma += milista[i]
               contador += 1
print("Ejercicio 2")
print("La suma de los números de la lista es", suma)
print("La cantidad de nros ingresados fue", contador)
print("El promedio de los números de la lista es", suma/contador)
print("----------------")      
               
#ejercicio 3. verifcar si es capicua 
capicua(milista)
print("----------------")

#ejercicio 4. buscar cuantas veces aparece un dato
print("Ejercicio 4")
z = int(input("Ingresar un valor a buscar en la lista "))
pos = buscardato(milista,z)
print("[",milista, "]")
print("El dato", z,"se encontró", pos,"veces en la lista.")

#ejercicio 5. función imprimir lista al réves
print("Ejercicio 5")
print("La lista impresa de atrás para adelante")
lista3 = imprimiralrevés(milista)
print("----------------")

#ejercicio 6. imprimir todas las posiciones ---- secuencial
print("Ejercicio 6")
c = int(input("Ingresar un valor a buscar en todas las posiciones de la lista "))
pos2= busquedasecuencial(milista,c)
print("----------------")


#ejercicio 7. imprimir todas las posiciones ---- binaria
import random
def cargarlista(cuantos):
    v = [ ]
    for i in range(cuantos):
        v.append(random.randint(1,100))
    return  v

def ordenar(v): #método de selección
    largo = len(v)
    for i in range(largo-1):
        for j in range(i+1,largo):
            if v[i] > v[j]:
                aux = v[i]
                v[i] = v[j]
                v[j] = aux
    return v

def busquedabinaria(lista,dato):
    izq= 0
    der = len(lista) - 1
    pos = -1
    while izq <= der and pos == -1:
        centro = (izq + der)//2
        if lista[centro] == dato:
            pos = centro
        elif lista[centro] < dato:
            izq = centro + 1
        else:
            der = centro -1
    return pos

#programa principal
print("Ejercicio 7")
print("¿Cuántos va a cargar?")
c = int(input("---> "))
milista = cargarlista(c)
print(milista)
#------------------------
lista1= ordenar(milista)
print("La lista ordenada")
print(lista1)
#------------------------
print("¿Qué dato quiere buscar en todas sus posiciones?")
dato = int(input("---> "))
pos = busquedabinaria(lista1,dato)
print("Se encontró el dato",dato,"en la posición",pos)

#ejercicio 8. Realizado
print("-------------")
print("Ejercicio 8")
import random
def cargarlsita():
    v = [ ]
    n = random.randint(0,100)
    while n != 0:
        v.append(n)
        n = random.randint(0,100)
    return v

def buscarmin(lista): #1. busco el minimo de TODA la lista
    largo = len(lista)
    min = 100 #este caso sabemos el máximo de toda la lista sino es 0
    i = 0
    while i <largo:
        if lista[i] < min:
            min = lista[i]
        i += 1
    return min

def imprimoelmin(lista,min): #2. imprimimos el minimo en TODAS sus posiciones
    largo = len(lista)
    if largo == 0: #si justo el primer nro es 0 no va a cargar nada el random.randint
        print("No se ingresaron valores a la lista.")
    else:
        print ("El minimo de la lista es", min)
        i = 0
        while i < largo: 
            if lista[i] == min: #si nuestro subíndice es el minimo
                print("Se encontró en la posición", i)
            i += 1 #permite hacerlo repetidas veces al ser un contador

#programa principal
lista1 = cargarlsita()
print(lista1)
print()
minimo = buscarmin(lista1)
lista2 = imprimoelmin(lista1,minimo)

#ejercicio 9. Método de inserción no entra
#ejercicio 10. no me salió
#ejercicio 11.
print("-------------")
print("Ejercicio 11")
import random
def cargarlista(cuantos):
    v = [ ]
    for i in range(cuantos):
        v.append(random.randint(1,100))
    return v
                 
def listac(a,b):
    vec = [ ]
    for i in range(len(a)):
        if a[i] % 2 == 0:
            vec.append(a[i])
    for i in range(len(b)):
        if b[i] % 2 != 0:
            vec.append(b[i])
    return vec

def listad(a,b):
    vec = [ ]
    for i in range(len(a)):
        if a[i] % 2 != 0:
            vec.append(a[i])
    for i in range(len(b)-1, -1, -1):
        if b[i] % 2 == 0:
            vec.append(b[i])
    return vec

def listae(a,b):
    vec = [ ]
    for i in range(len(a)):
        vec.append(a[i])
        vec.append(b[i])
    return vec

#programa principal
print("¿Cuántos elementos quiere cargar en la lista A?")
x = int(input("---- "))
listaA = cargarlista(x)
print(listaA)
print("¿Cuántos elementos quiere cargar en la lista B?")
y = int(input("---- "))
listaB = cargarlista(y)
print(listaB)
            
print()
listaC = listac(listaA,listaB)
print("Lista C (nros pares de ListaA y nros impares de ListaB): ", listaC)
listaD = listad(listaA,listaB)
print("Lista D (nros impares de Lista A y nros pares al revés de Lista B): ", listaD)
listaE = listae(listaA,listaB)
print("Lista E (intercalación de ambas listas): ", listaE)
#ejercicio 12.
def metododeintercambio(v): #o de burbujeo
    desordenado = True
    while desordenado:
        desordenado = False
        for i in range(len(v)-1):
            if v[i]>v[i+1]:
                aux = v[i]
                v[i] = v[i+1]
                v[i+1] = aux
                desordenado = True
    return v
                                             
#programa principal
print("-------------")
print("Ejercicio 12")
listaA = [3, 10, 15, 17, 27, 29]
n = int(input("Ingresar nro para añadir a la lista "))
listaA.append(n) # se agrega el nro a nuestra lista

listaB = metododeintercambio(listaA) # ya se agrego el nro previamente
print("La lista final es ", listaB)
#ejercicio 13. ordenar sin método????
def metododeburbujeo(a,b): #ordenar las dos al mismo tiempo
    desordenado = True
    while desordenado:
        desordenado = False
        for i in range(len(b)-1):
            if b[i] > b[i+1]:
                aux = b[i]
                b[i] = b[i+1]
                b[i+1] = aux
                
            if a[i] > a[i+1]:
                aux = a[i]
                a[i] = a[i+1]
                a[i+1] = aux
                
                desordenado = True
    
    return a, b

#programa principal
lista1 = [15, 27, 10, 17, 29]
lista2 = [12, 4, 10, 5, 10]
ordenada = metododeburbujeo(lista1,lista2)
print("Ambas listas ordenadas de menor a mayor")
print(ordenada)
print( )
print("La nueva lista con los elementos intercalados sin un método")
print("chupala")

#ejercicio 14. necesito saber cuantos cumplen en cada mes y el que mas cumplen

nrodelegajo = int(input("Nro de legajo del alumno (-1 para terminar) "))
cump=[0,0,0,0,0,0,0,0,0,0,0,0,0] #cada mes tiene una variable iniciada en cero
mayor = 0


if nrodelegajo == -1:
    print("No se ingresaron valores")
else:
    while nrodelegajo != -1:
        print("¿Fecha de Cumpleaños?")
        d = int(input("Día: "))
        m = int(input("Mes: "))
        a = int(input("Año: "))
        i = m
        cump[i] += 1 #contador de cada mes
        if cump[i] > mayor:
            mayor = cump[i]
        nrodelegajo = int(input("Nro de legajo del alumno (-1 para terminar) "))
    print( )

for i in range(1,13):
    print("En el mes", i,"cumplen", cump[i],"alumnos.")

print()

for i in range(1,13):
    if mayor == cump[i]:
        print("El mes",mayor,"cumplen la mayor cantidad de alumnos.")
