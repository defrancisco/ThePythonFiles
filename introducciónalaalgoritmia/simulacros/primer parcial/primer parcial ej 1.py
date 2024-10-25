"""Ejercicio 1
Se ingresa por teclado el nro de legajo de los alumnos de un curso y su nota de examen final.
El fin de la carga se determina ingresando un -1, en la variable del legajo.
Se debe validar que la nota ingresada sea entre 1 y 10.
Se pide informar:
a)  Cantidad de alumnos con nota >= 7
b)  Cantidad de alumnos con nota >= 4 y <7
c)  Porcentaje de alumnos que están aplazados.
d)  Cantidad total de alumnos.
e)  La nota más alta.

"""
legajo = int(input("Ingresar nro de legajo o -1 para terminar  "))
#VARIABLES
promociona = 0
aprueba = 0
no = 0
mayor = 0
legajomayor = 0
alumno = 0
while legajo!= -1:
    nota = int(input("Ingresar nota del final  "))
    while nota <1 or nota >10:
        print("Ingresar una nota válida ")
        nota = int(input("Ingresar nota del final  "))
    if nota >= 7:
        promociona += 1 #contador
    elif nota >= 4 and nota<7:
        aprueba += 1
    else:
        no += 1
        
    if nota > mayor:
        mayor = nota
        legajomayor  = legajo
    alumno +=1 #contar la cantidad de alumnos ingresados
    legajo = int(input("Ingresar nro de legajo o -1 para terminar  "))

#programa principal
if alumno != 0:
    print("--------------------------------------------------------------------------------------------------------------------")
    print("Cantidad de alumnos que se sacaron siete o más de siete ---> ", promociona)
    print("Cantidad de alumnos que se sacaron entre siete y cuatro ---> ", aprueba)
    print("Cantidad de alumnos que se sacaron menos de cuatro ---> ", no)
    print("Cantidad de alumnos ingresados --->", alumno)
    print("El alumno", legajomayor, "obtuvo la mejor nota", mayor)
    print("Promedio de alumnos aplazados", (no*100)/alumno )
else:
    print("no se ingresaron valores")