"""Un número pandigital es aquel que contiene todos los dígitos del 0 al 9 al menos una vez, como el 1023478695. Escribir una función esPandigital(n) que determine si un número n es pandigital, retornando True o False según corresponda. Escribir también un programa para ingresar un número, invocar a la función y mostrar un mensaje informativo.

Ejemplos:

• El número 2424643 no es pandigital, por lo la función debería retornar False.
• El número 10123485769 cumple que es pandigital, por lo que debería retornar True.
"""

def espandigital(nro):
    "Con cadenas"
    es_pandigital = True
    digitos = list("0123456789")
    numero = str(nro)
    for digito in digitos:
        if digito not in numero:
            es_pandigital = False
    return  es_pandigital

 
#programa principal
n1 = 2424643 #false
n2 = 101234856769 #true
print(espandigital(n1))
print(espandigital(n2))