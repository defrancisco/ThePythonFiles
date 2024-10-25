# Escribir una función que reciba como parámetros la fecha de nacimiento de una persona y la fecha actual, y devuelva la edad de la persona.
def leerentero (min, max):
    print("Ingrese un número entre", min, "y", max, end="")
    a = int(input()) # ¿por qué el msj no se muestra aquí?
    while a<min or a>max:
        print("Valor incorrecto. Debe estar entre", min, "y", max)
        a= int(input("Ingrese un número entero:"))
        return a
    
def calcularedad(dnac, mnac, anac, dact, mact, aact):
    edad = aact - anac
    if mact < mnac:
        edad = edad -1
    elif mact == mnac and dact < dnac:
        edad = edad -1
        return edad
    
#Programa principal
print("Ingrese el día de nacimiento:")
dnac = leerentero(1,31)
print("Ingrese el mes de nacimiento:")
mnac = leerentero(1, 12)
print("Ingrese el año de nacimiento:")
anac = leerentero(1583, 2100)
print("Ingrese el día de hoy")
dhoy = leerentero(1, 31)
print("Ingrese el mes de hoy:")
mhoy = leerentero(1, 12)
print("Ingrese el año de hoy:")
ahoy= leerentero(1583,2100)
edad= calcularedad(dnac, mnac, anac, dhoy, mhoy, ahoy)
print("Ud. tiene", edad, "años")

