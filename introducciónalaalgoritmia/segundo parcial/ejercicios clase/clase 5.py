# ejemplo 1 : cálculo de un promedio
#función
def calcularpromedio (a,b): #parámetros formales 
    total = (a + b)/2 
    return total #instrucción que siempre esta 

#programa principal. recordar LLAMAR a la función en el pp
x = int(input("Ingrese un número entero:"))
y = int(input("Ingrese otro número entero:"))
resultado= calcularpromedio(x,y) # parámetros reales 
print("El promedio de", x, "y", y, "es", resultado)

# suma y resta
def calcularresta (a,b):
    total= (a-b)
    return total

def  calcularsuma (a,b):
    suma= (a+b)
    return suma

x= int(input("Ingrese un número entero:"))
y= int(input("Ingrese un número entero:"))
resta= calcularresta(x,y)
suma= calcularsuma(x,y)

print("El resultado de la resta de", x, "y", y, "es", resta)
print("El resultado de la suma de", x, "y", y, "es", suma)

# ejemplo 2 : Escribir una función para ingresar un número entero a través del teclado, verificando que éste se encuentre dentro de los límites permitidos.
# ejemplo 3 : Escribir una función que reciba como parámetros la fecha de nacimiento de una persona y la fecha actual, y devuelva la edad de la persona.
# ejemplo 4 : Ingresar por teclado tres números enteros correspondientes a una fecha y devolver la fecha ingresada como valor de retorno.
# ejemplo 5 : Imprimir una fecha recibida como parámetro. ¿Qué valor tenemos que devolver?

def leerentero (min, max): # función para ingresar y validar los números EJERCICIO 2
    print("Ingrese un número entre", min, "y", max, " ", end="")
    a= int(input())
    while a<min or a>max:
        print("Valor incorrecto. Debe estar entre", min, "y", max)
        a= int(input("Ingrese un número entero "))
    return a

def calcularedad (dnac, mnac, anac, dact, mact, aact): #función para saber la edad EJERCICIO 3
    edad= aact - anac
    if mact<mnac:    #si el mes actual es menor que el mes de nacimiento se descuenta el año
        edad = edad - 1
    elif mact ==mnac and dact<dnac : #si el mes actual es el mimso al del nacimiento pero la fecha es menor a la de nacimiento se descuent aun año
        edad = edad - 1
    return edad

#programa principal
print("Ingrese el día de nacimiento ")
dnac = leerentero(1,31)
print("Ingrese el mes de nacimiento ")
mnac = leerentero(1,12)
print("Ingrese el año de nacimiento ")
anac = leerentero(1500, 2100)
print("Ingrese el día de hoy ")
dhoy = leerentero(1, 31) #esta información se ingresa en la función como "actual"
print("Ingrese el mes de hoy ")
mhoy = leerentero(1,12) #esta información se ingresa en la función como "actual"
print("Ingrese el año de hoy ")
ahoy = leerentero(1500,2100) #esta información se ingresa en la función como "actual"

edad= calcularedad(dnac, mnac, anac, dhoy, mhoy, ahoy)
print("Ud. tiene", edad, "años.")

# ejemplo 6: Imprimir una fecha recibida como parámetro. ¿Qué valor tenemos que devolver?
def imprimirfecha(d, m , a):
    print("La fecha es",d,"/", m, "/", a)
    imprimirfecha(día, mes, año)

print("Ingrese el día ")
dact = imprimirfecha(1,31)
print("Ingrese el mes ")
mact = imprimirfecha(1,12)
print("Ingrese el año ")
anac = imprimirfecha(1500, 2100)

# ejemplo 7 : Imprimir una columna de asteriscos, donde su altura se recibe como parámetro usando una función.
def imprimiraltura(a):
    n=0 #contador
    while n<a:
        print("*")
        n= n + 1

altura= int(input("Ingrese una altura "))
imprimiraltura(altura)

# ejemplo 8 : Realiza una función llamada relacion(a, b) que a partir de dos números cumpla lo siguiente:
 # Si el primer número es mayor que el segundo, debe. Si el primer número es menor que el segundo, debe devolver -1. Si ambos números son iguales, debe devolver un 0. Solo se pueden ingresar valores positivos
 
 # FUNCIÓN
def relacion(a, b):
    if a>b:
        return 1 # si es devolver y en la función es return
    elif a<b:
        return -1
    else:
        return 0

#CÓDIGO PRINCIPAL CON LOS INTS
nro1 = int(input("Ingrese un número positivo "))
while nro1<0: # verificar que sea nro positivo
    nro1 = int(input("Error. Ingrese un número positivo "))
nro2 = int(input("Ingrese un número positivo "))
while nro2<0:
    nro2 = int(input("Erro. Ingrese un número positivo "))
    
resultado = relacion(nro1,nro2)
print(resultado)

#PRINTS
if resultado ==1:
    print("el primer número es mayor que el segundo", nro1,nro2)
elif resultado==-1:
    print("el primer número es menor que el segundo", nro1,nro2)
else:
    print("ambos números son iguales", nro1,nro2)
 
# ejemplo 9 : Escribir una función que, dado un numero de DNI,retorne True si el número es válido y False si no lo es.
 # Para que un numero de DNI sea válido debe tener entre 7 y 8 dígitos.
 
 def leerDNI(dni):  #FUNCIÓN 
    cantidad = 0
    while dni != 0:
        cantidad += 1
        dni = dni //10 #saber cuántos números tienen
    if cantidad == 7 or cantidad == 8 :
        return  True
    else :
        return  False
    
#CÓDIGO PRINCIPAL
dni = int(input("Ingrese su DNI  "))
if leerDNI(dni):
    print("El DNI", dni, "es válido.") #cada print se va a acopalr al primer if/else de la función principal
else:
    print("El DNI", dni, "es inválido.")