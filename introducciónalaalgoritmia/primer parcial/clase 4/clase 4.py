# imprimir los números enteros entre 1 y 100
a = 1
while a <= 100:
    print(a)
    a = a + 1 #línea que incrementa el contador
    #fin del programa

# imprimir los números pares entre 1 y 100
a = 2
while a <= 100:
    print(a)
    a = a + 2
    #fin del programa
    
# pide un número postivo al usuario una y otra vez hasta que el usuario lo haga correctamente:
número=int (input("Escriba un número positivo:"))
while número <0:
    print("¡Ha escrito un número negativo! Inténtelo de nuevo")
    número= int(input("Escriba un número positivo:"))
    print("Gracias por su colaboración") #este es el final

# leer un conjunto de números enteros e imprimir su promedio. El fin de los datos se indica ingresando el valor -1.
suma= 0
cant= 0
n= int(input("Ingrese un número o -1 para terminar:")) #el -1 corta el búcle
while n !=-1: #! es diferente
    suma= suma + n
    cant= cant + 1
    n= int(input("Ingrese un número o -1 para terminar:"))
    
 if cant!= 0:
    prom= suma/cant #promedio. fórmula
    print("El promedio es", prom)
 else:
    print("No se ingresaron valores") #si lo primero que pones es -1

# leer un conjunto de números enteros e impimir el mayor. El fin de los datos se indica con -1.
n = int(input("Ingresar un número entero o -1 para terminar:"))
mayor= n #se guarda el número
while n != -1:
    if n > mayor:
        mayor = n
    n = int(input("Ingrese un número entero o -1 para terminar:")) #se continúa el ciclo
    print("El mayor es", mayor)
    

<<<MAL EJECUTADOS>>>
    
# leer notas de 35 alumnos de una clase, establecidas entre o y 10. Se desea desarrollar el pseudocódigo, diagrama de flujo y lenguajes Python para un programa que determine la nota promedio.
d= 1 
suma= 0 
while d<36: #cantidad justa de ingresos
    nota= int(input("Ingresar nota de alumno:"))
    suma= suma+nota
    d= d + 1
    print("El promedio de 35 alumnos es:", suma/35)
    
# tabla de multiplicar
número= int(input("Ingrese número:"))
i= 1 #con lo que empieza a multiplicar
LIMITE=10 #con lo que va a multiplicar por
while i<=LIMITE:
    resultado= i*número
    print(número, "x", i, "=", resultado)
    i= i + 1
    