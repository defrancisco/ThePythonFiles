#Determinar si un número entero es par o impar.
x = int(input("Ingrese un número:"))
if x % 2 == 0:
    print(x, "es par")
else:
    print(x, "es impar")


#Leer un número e informar si es postivo, negativo o cero.
n = int(input("Ingrese un número entero:"))
if n > 0:
    print("El número es positivo:")
elif n < 0:
    print("El número es negativo")
else:
    print("El número es cero")

#Ejemplo n°5
edad = int(input("Ingresar edad:"))
if edad >= 18:
    print("Es mayor de edad")
elif edad < 0:
    print("Imposible flaco")
else:
    print("Es menor de edad")

#Leer por teclado tres números enteros distintos y mostrar el mayor.
nro1= int(input("Ingrrese un número:"))
nro2= int(input("Ingrrese un número:"))
nro3= int(input("Ingrrese un número:"))

if nro1>nro2 and nro1>nro3:
    print("El número mayor es:", nro1)
else:
 if nro2>nro3:
        print("El número mayor es:", nro2)
 else:
    print("El número mayor es:", nro3)
    
#La carga de una fecha se hace por partes, ingresamos las variables dia, mes y año. Mostramos el msj ¨Corresponde al primer trimestre¨en caso que el mes ingresado por teclado sea igual a 1, 2 ó 3. En la condicón no participan las variables día y año.
día= int(input("Ingrese nro de día:"))
mes= int(input("Ingrese nro de mes:"))
año= int(input("Ingrese nro de año:"))

if mes == 1 or mes ==2 or mes ==3:
    print("Corrresponde al primer trimestre")
else:
    print("No Corresponde al primer trimestre")

#Leer un número entero e imprimir un mensaje indicando. Si corresponde a un número válido de mes.
mess= int(input("Ingrese un número de mes:"))
if mess >= 1 and mess <=12:
    print("El mes es válido")
else:
    print("El mes no es válido")


# entrada salida para declarar asignar y el if
    