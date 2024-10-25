"""CLASE NRO 5: programación modular,
funciones, valores de retorno, ámbito de las variables"""

#función --- módulo ind de programa que realiza una tarea específica

#ejemplo 1 : calcular un promedio
def calcularpromedio(a,b):
    p = (a + b ) / 2
    return p

#programa principal
x = int(input("Ingresar un nro  "))
y = int(input("Ingresar otro nro  "))
print( ) #prolijidad del código
promedio = calcularpromedio(x,y) #recordar llamar y darle un valor a la función
print("El promedio de los nros ingresados es", promedio)

#ejemplo 2: ingresar un nro entero y verificar
def leerentero(min,max):
    print("Ingrese un nro entero que se encuentre entre", min ,"y",max)
    a = int(input("---> " )) #donde ingresaremos los datos
    if  a<min or a>max:
        print( )
        print("Error. Ingrese un nro válido según los criterios")
        print("Ingrese un nro entero que se encuentre entre", min ,"y",max)
    return a

def calcularedad(dnac, mnac, anac, dact, mact, aact):
    edad = aact - anac
    if mact < mnac:
        edad = edad - 1
    elif mact == mnac and dact < dnac:
        edad = edad - 1
    return edad
        
#programa principal para ingresar los nros se conecta con la primera función
print("Ingresar día de nacimiento") #primero
dian = leerentero(1,31) #segundo: parámetro + lugar done ingresa el dato
print("Ingresar mes de nacimiento")
mesn = leerentero(1, 12)
print("Ingresar año de nacimiento")
añon = leerentero(1500,2100)
print("Ingresar día actual")
dhoy= leerentero(1,31)
print("Ingresar mes actual")
dmes= leerentero(1,12)
print("Ingresar año actual")
daño = leerentero(1500,2100)

años = calcularedad(dian, mesn, añon, dhoy, dmes, daño)
print()
print("Ud. tiene", años,"años.")

#ejemplo 6: imprimir una fecha recibida como parámetro
def leerfecha(min,max):
    print("Los nros deben estar entre", min, "y", max)
    i =int(input("--->"))
    if i<min or i>max:
        print("Valor inválido. Revisar los parámetros")
        print("Los nros deben estar entre", min, "y", max)
    return i

def imprimirfecha(d, m, a):
    print("La fecha de hoy es ",d,"/",m, "/",a)


#programa principal
print("--Hoy--")
print()
print("Ingrese el día")
día = leerfecha(1,31)
print("Ingrese el mes")
mes = leerfecha(1,12)
print("Ingrese el año")
año = leerfecha(2002,2023)

imprimirfecha(día, mes, año)

#ejemplo 7: ingrese una altura e imprimirla con algo
def imprimiraltura(a):
    h = 0
    while h<a:
        print("<3")
        h += 1
    
#programa principal
altura = int(input("Ingresar altura a imprimir   "))
height = imprimiraltura(altura)

#ejemplo 8: ingresar dos nros, ver relación y verificar que sean positivos
def relacion(a,b):
    if a>b:
        return 1
    elif a<b:
        return -1
    else:
        return 0
    
#programa principal
x = int(input("Ingresar el primer nro "))
while x<0:
    print("Error. Ingrese un nro positivo.")
    x = int(input("Ingresar el primer nro "))
y = int(input("Ingresar el segundo nro "))
while y<0:
    print("Error. Ingrese un nro positivo.")
    y = int(input("Ingresar el segundo nro "))

re= relacion(x,y)

#prints
if re == 1:
    print("El primero es mayor que el segundo")
elif re == -1:
    print("El segundo es mayor que el primero")
else:
    print("Los nros son iguales")

#ejemplo 9: validar DNI

def validación(doc):
    cont = 0
    while doc != 0: #primero que haya nros ingresados
        cont += 1#contador que nos va a decir la cantidad de nros
        doc //= 10 #fórmula para sacar los digitos
    if cont == 7 or cont == 8: # el contador es quien válida
        return True
    else:
        return False

#programa principal
print("Ingrese su nro de DNI")
dni = int(input("---> "))
resultado = validación(dni)
if resultado == True:
    print("Su DNI", dni,"es válido.")
else:
    print("Su DNI", dni, "es inválido.")