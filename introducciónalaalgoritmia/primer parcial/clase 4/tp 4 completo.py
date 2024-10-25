#1.
n =int(input("Ingresar números o finalizar con -1 "))
#variables
primero= n #ojo!!
último= 0 

while n != -1:
    último= n + 0
    n =int(input("Ingresar números o finalizar con -1 "))

#prints
print("El primer número es ", primero)
print("El último número es ", último)

#2. ERROR
n = int(input("Ingresar números o finalizar con -1 "))

while n != -1:
    n = int(input("Ingresar números o finalizar con -1 "))
    if n % 2 == 0:
        print("Son pares")
    else:
        print("Son impares")

#3. REPASAR!!!!
valor=int(input("ingrese un nro "  ))
#contadores 
mayor=valor 
menor=valor

if valor == -1: #dice finalizar la lectura de datos
    print("No se ingresaron valores")
else:
    while valor != -1: #todo el búle a la misma altura
        if mayor<valor: 
            mayor=valor
        if menor>valor:
            menor=valor
        valor=int(input("ingrese un nro"  ))
    print("El valor menor es: ",menor,"y el valor mayor es ",mayor) #todos los prints a la misma altura
    
#4.
n = 42

while n <=174:
    if n%2 != 0:
        print(n)
    n = n + 1
    
#5.
n = int(input("Ingresar número "))
        
num= 1 #entre 1 y N

while num < n:
        num = num + 1
        print(num)
        
#6. PRESTAR ATENCIÓN
número= int(input("Ingresar número a multiplicar "))
i = 1 #con lo que se empieza a multiplicar
límite = 12 # con lo máximo que se multiplica.

while i<=límite:
    resultado= i * número
    print(número,"x", i ,"=", resultado)
    i = i + 1
    
#7. 

mayor= 0
suma= 0
contador= 0
posición= 0


while contador<=10: #prestar atención
    n = int(input("Ingresar un número entero "))
    if n>mayor:
        posición = contador
        mayor= n
    contador= contador + 1
    suma= suma + n
    
promedio= suma/10

print("El mayor es ", mayor)
print("Posición en que estaba ", posición )
print("El promedio es ", promedio) 

#8.
suma= 0
contador= 0

while suma !=100: #LOS LÍMITES SE EXPRESAN CON DIFERENCIA
    n= int(input("Ingresar números par "))
    if n%2 == 0:
        suma= suma + n
        contador= contador + 1
          
print("Cantidad de número ingresados", contador)

#9.
n = int(input("Ingresar la terminación de la patente o terminar con -1 "))
par= 0
impar= 0

while n != -1:
    if n>=0 and n<=9:
        if n % 2 ==0:
            par= par + 1 #contador
        if n % 2 !=0:
            impar= impar + 1 #contador
        n = int(input("Ingresar otra terminación de la patente o terminar con -1 ")) #prestar atención donde poner devuelta el requerimiento
    else:
        print() #espacios
        print("Ingresar una patente entre 0 y 9.")
        print()
        n = int(input("Ingresar una neuva terminación de patente:"))
        
print("--------------------------------------")
print("Cantidad de autos con patente par", par)
print("Cantidad de autos con patente impar", impar)

#a partir de acá no son mis ejercicios son de alguien más pero supongo que estan bien.

#10. QUÉ MIERDA ES UN FACTORIAAAAALLLLL
N = int(input("Ingresar número ")) #factorial: nro positivo
factorial = 1
aux = 0

if N<0:
    while N<0 or N%2 !=0:
        print("Ingresar un número ")
    aux= N
    while N>0:
        factorial = factorial * N
        N = N - 1
        
else:
    aux= N
    while n>0:
        factorial=factorial*n
        n=n-1
        
print("El factorial de",aux,"es igual a:",factorial)

#11.
n=int(input("Ingrese un numero: "))
contdiv=0
division=1

while division<=n:
    if n%division==0:
        contdiv=contdiv+1
        division=division+1
    else:
        division=division+1
        
if contdiv>2:
    print ("El numero es compuesto")
else:
    print ("El numero es primo")

#12.chupala