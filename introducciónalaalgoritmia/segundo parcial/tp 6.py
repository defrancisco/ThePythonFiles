"""Trabajo Práctico 6: Funciones"""
#ejercicio 1:
def multisuma(a,b):
    conta = 0
    suma = 0
    while conta != b:
        conta += 1 #contador para saber cuantas veces me queda
        suma += a #aca se hace la "multiplicación"
    return suma
    
#programa principal
x = int(input("Ingresar nro ---  "))
y = int(input("Ingrese nro multiplicador  ---  "))
resultado = multisuma(x,y)
print()
print("El resultado de ", x, "x", y," es ", resultado)

#ejercicio 2:
def elevar(a,b):
    cont = 0
    pro= 1 #producto arranca con 1 y es el valor a devolver
    while cont != b:
        cont += 1
        pro *= a
    return pro

#programa principal
x = int(input("Ingresar nro ---  "))
y = int(input("Ingrese nro a elevar por  ---  "))
resultado = elevar(x,y)
print()
print("El resultado de ", x, "*", y," es ", resultado)

#ejemplo 3: columna
def imprimiraltura(a):
    n = 0
    while n<a:
        print("<3")
        n += 1 #contador

#programa principal
print("Ingresar altura")
altura =  int(input("---> "))
height = imprimiraltura(altura)

#ejercicio 4: multiplo a%b == 0
def esmultiplo(a, b):
    if a%b==0:
        return True
    else:
        return False
    
#programa principal
print("---Ingrese los nros a verificar si son múltiplos---")
x = int(input("Primer nro "))
y = int(input("Segundo nro "))
resultado= esmultiplo(x,y)
print()
if resultado == True:
    print("True")
    print("Los nro ingresados son múlplos.")
else:
    print("False")
    print("Los nros ingresados no son múltiplos")
    
#ejercicio 5: signos
def signo(n):
    if n>0:
        return 1
    elif n<0:
        return -1
    else:
        return 0
    
#programa principal
nro = int(input("Ingrese un nro "))
num = signo(nro)
if num == 1:
    print("--- es positivo")
elif num == -1:
    print("--- es negativo")
else:
    print("--- es nulo")

#ejercicio 6: mayor/menor
def comparar(a,b):
    if a>b:
        return 1
    elif b>a:
        return -1
    else:
        return 0

#programa principal
print("--- Compare Números ---")
x = int(input("Ingrese el primer nro "))
y = int(input("Ingrese el segunro nro "))
r = comparar(x,y)
print()
if r == 1:
    print("1")
    print("El primero es mayor que el segundo")
elif r == -1:
    print("-1")
    print("El segundo es mayor que el primero")
else:
    print("0")
    print("Los número ingresados son iguales")
    
#ejercicio 7: máximo común divirsor. mientras b - a, b = b, a % b
def mcd(a,b):
    while b:
        a , b = b, a % b
    return a

x = int(input("Ingrese el primer número: "))
y = int(input("Ingrese el segundo número: "))
t= mcd(x,y)
print()
print("El MCD de", x, "y", y, "es", t )

#ejercicio 8: matemática = no hago ingeniería por una razón y es esta

#ejercicio 9: fechas. esta gauchito porque arriba lo justifica
def ingresarfecha(min, max):
    print("Ingresar nro entre", min, "y", max)
    f = int(input("---- "))
    print( )
    while f < min or f >max:
        print("ERROR. ingresar nros válidos")
        print("Ingresar nro entre", min, "y", max)
    return f

def calcularfindemes(dia,mes):
    if mes == 1 or mes == 3  or mes == 5 or mes == 7 or mes == 10 or mes == 12:
        faltan = 31 -  dia
    elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
        faltan = 30 - dia
    else:
        faltan = 28 - dia
    return faltan

def calcularfindeaño(daño):
    dd = 365 - daño
    return dd

    
#programa principal
print("¿Cuánto falta para fin de año?")
print("Día actual")
dhoy = ingresarfecha(1,31)
print("Mes actual")
mhoy = ingresarfecha(1,12)
print("Año actual")
ahoy = ingresarfecha(2022,2023)

findemes = calcularfindemes(dhoy, mhoy)
print("Faltan", findemes,"días para fin de mes")
print()
print("¿Qué día del año es?")
print("Ingresar que día del año es")
daño= ingresarfecha(1,365)
findeaño = calcularfindeaño(daño)
print("Faltan", findeaño,"días para el fin del año")

#ejercicio 10: extraer digito de derecha a izquierda
def extraerdigito(num, pos):
    cont = 0
    while cont <= pos:
        digito = num % 10 #saber cuantos hay
        num //= 10
        cont += 1
    if num == 0 and digito == 0:
        return -1
    else:
        return digito

#programa principal
print("Extraer un dígito de un número")
x = int(input("Ingrese nro a extraer --- "))
y = int(input("Ingrese cifra a buscar  --- "))
r = extraerdigito(x,y)
if r == -1:
    print("-1")
    print("El digito solicitado no existe")
else:
    print("El digito solicitado", x, "es", r)
    
#ejercicio 11. devoler central solo si es impar IMPOSIBLE BOLUDO
def devolvercentral(nro):
    cont= 0
    devolver = -1
    nroOriginal = nro
    while nro> 0:
        digito = nro%10
        cont+=1
        nro=nro//10
    print("cantidad de digitos del numero" ,cont)
    if (cont%2) != 0:
        posicioncentral= cont//2
        cont= 0
        
        while nroOriginal >0 and devolver == -1:
            digito= nroOriginal%10
            if cont == posicioncentral:
                devolver = digito
            cont +=1
            nroOriginal = nroOriginal //10
    return devolver
        

#programa principal
    
numero = int(input("ingrese un numero: "))
valorcentral= devolvercentral(numero)
if valorcentral == -1:
    print("el numero no tiene cantidad impar de digitos")
else:
    print("el digito central es " ,valorcentral)