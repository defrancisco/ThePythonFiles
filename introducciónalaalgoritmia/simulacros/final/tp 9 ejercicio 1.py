"""Ejercicio 1: Leer los números de legajo de los alumnos de un curso y su nota de examen final. Cargar el
número de legajo en la lista LEGAJOS y la nota en la lista NOTA_FINAL. El fin de la carga se
determina ingresando un -1 como legajo. Se debe validar que la nota ingresada sea entre 1 y
10. Terminada la carga de datos, recorrer las listas e informar:
▪ Cantidad de alumnos que aprobaron con nota mayor o igual a 4
▪ Cantidad de alumnos que desaprobaron el examen. Nota menor a 4
▪ Promedio de nota y los legajos que superan el promedio
Luego se solicita, ordenar las listas según el número de legajo, de manera ascendente
Ingresar un nro de legajo e informar la nota del examen final utilizando busqueda binaria"""


def cargarlista( ):
    nro = int(input("Nro de legajo (-1 para terminar): "))
    if nro == -1:
        print("No se cargaron números de legajos.")
    else:
        while nro != -1:
            nota = int(input("Nota Examen Final: "))
            if nota < 1 or nota > 10:
                print("*ERROR*. Ingresar nota válida")
            else:
                legajos.append(nro)
                nota_final.append(nota)
                nro = int(input("Nro de legajo (-1 para terminar): "))
                
def metododeintercambio(v,b):
    desordenado = True
    while desordenado:
        desordenado = False
        for i in range(len(v)-1):
            if v[i] > v[i+1]:
                aux = v[i]
                v[i] = v[i+1]
                v[i+1] = aux
            if b[i] > b[i+1]:
                aux = b[i]
                b[i] = b[i+1]
                b[i+1] = aux
                desordenado = True
    return v, b

def busquedabinaria(v,dato):
    izq= 0
    der = len(v)
    pos = -1
    while izq <= der and pos == -1:
        centro = (izq+der) //2
        if v[centro] == dato:
            pos = centro
        elif v[centro] < dato:
            izq= centro +1
        else:
            der = centro + 1
    return pos

#programa principal
legajos = [ ]
nota_final = [ ]
aprobados, desaprobados, superior, suma = 0, 0, 0, 0
lista = cargarlista()


for i in range(len(legajos)):
        if nota_final[i] >= 4:
            aprobados +=1
        else:
            desaprobados +=1
        suma += nota_final[i]
promedio = suma/ len(legajos)        
print()
print("Cantidad de alumnos desaprobados", desaprobados)
print("Cantidad de alumnos aprobados", aprobados)
print("Promedio de notas", promedio)
for i in range(len(legajos)):
    if nota_final[i] > promedio:
        superior = legajos[i]
        print("Alumno que supero el promedio", superior)

#ordenar listas según el nro de legajo
print("---------------------------------------")
print("Listado de Alumnos por Número de Legajo")
ordenar = metododeintercambio(legajos, nota_final)
for i in range(len(legajos)):
    print("Número de Legajo:", legajos[i], "Califiación:", nota_final[i])
    
# meto legajo saco nota
print("---------------------------------------")
num = int(input("Buscar alumno por legajo:  "))
p = busquedabinaria(legajos, num)
if p!=-1:
    print ("Alumno:", legajos[p],"Nota Examén Final:", nota_final[p])
else:
    print ("el legajo no se encontro en la lista")