#1.

edad = int(input("Ingresar edad o terminar con -1 "))

menores= 0
mayores= 0
suma_mayores= 0
suma_menores= 0

while edad != -1:
    edad = int(input("Ingresar otra edad o terminar con -1 "))
    while edad <=0 and edad >=100:
        print("Edad no válida")
        edad = int(input("Ingresar edad o terminar con -1 "))
    if edad<18:
        menores = menores + 1
        suma_menores= suma_menores + edad
    elif edad>=18:
        mayores = mayores + 1
        suma_mayores= suma_mayores + edad
    else:
        print("error")
    
if menores > 0 and mayores > 0:
    print()
    print("Cantidad de menores ", menores)
    print("Promedio ", suma_menores*100/menores)
    print()
    print("Cantidad de mayores ", mayores)
    print("Promedio ", suma_mayores*100/mayores)
else:
    print("Error.")
    
#2.

nrolegajo = int(input("Ingresar legajo o terminar con -1 "))

aprueba= 0
desaprueba= 0
aplazado= 0
cantidadalumnos = 0

while nrolegajo != -1:
    notafinal = float(input("Ingresar otra nota de examen final "))
    while notafinal<1 or notafinal>10:
        print("Ingresar una nota válidad")
        notafinal = float(input("Ingresar nota válida de examen final "))
    if notafinal >=4:
        aprueba= aprueba + 1
    elif 2 <= notafinal <= 3:
        desaprueba = desaprueba + 1
    elif notafinal ==1:
        aplazado= aplazado + 1
    else:
        print("No se ingresaron valores")
    cantidadalumnos= cantidadalumnos + 1
    nrolegajo = int(input("Ingresar legajo o terminar con -1 "))

if cantidadalumnos !=0:
    print()
    print("Cantidad de alumnos que aprobaron el examen con nota mayor o igual a 4 ", aprueba)
    print("Cantidad de alumnos que desaprobaron el examen con nota menor a 4 ", desaprueba)
    print("Porcentaje de alumnos que están aplazados (tienen 1 en el examen) ", aplazado*100/cantidadalumnos)
else:
    print("No se ingresaron números,")
    
#3.No esta bien bien peeero funciona
    producto = int(input("Ingresar cantidad de producto o termianr con - 1 "))


#descuento1= .10 #13 y 100
#descuento2= .25 #100
unidad1 = 0
unidad2= 0
ventas= 0
docena= 0

while producto != -1:
    preciobase = int(input("Ingresar precio base  "))
    if producto<=12:
        docena= docena + 1
    elif 13 <= producto <=100:
        unidad1= unidad1 + 1
    elif producto>100:
        unidad2= unidad2 + 1
    else:
        descuento1= unidad1*10/100
        descuento2= unidad2*25/100
    ventas= ventas + 1
    producto = int(input("Ingresar cantidad de producto o termianr con - 1 "))
       

if total != 0:
    print()
    print("Cantidad de ventas realizadas total ", ventas)
    print("Cantidad de ventas en las que se aplicó un 10% de descuento ", unidad1)
    print("Cantidad de ventas en las que SOLO se aplicó el precio base, es decir que no se le realizaron descuentos ", docena)
    print()
else:
    print("error.")
    
#4.
    
nrocliente = int(input("Ingresar número de cliente o -1 para terminar "))
while nrocliente != -1:
    totalfactu = int(input("Ingresar total de la factura "))
    nrocliente = int(input("Ingresar número de cliente o -1 para terminar "))
    aprimeros10 = totalfactu - 200
    bprimero10= totalfactu*2/100
    siguientes10= totalfactu
    aveintedías= totalfactu + 350
    bveintedías= totalfactu *10/100

print("Número de Cliente", nrocliente )
print("importe 1 ",aprimeros10, "|", bprimero10)
print("Importe 2 ",siguientes10)
print("Importe 3",aveintedías, "|", bveintedías)

#5.
D= int(input("Ingresar día "))
M= int(input("Ingresar mes "))
A= int(input("Ingresar año "))
totaldías= int(input("¿Cuántos días desea sumarle? "))

n=1

while n<=totaldías:
    if M==1 or M==3 or M==5 or M==7 or M==8 or M==10 or M==12:
        cantidaddías= 31
    elif  M==4 or M==6 or M==9 or M==11:
        cantidaddías=30
    elif M==2:
        if(A%4==0 and A%100!=0) or A%400==0:
            cantidaddías=29
        else:
            cantidaddías= 28
    else:
        cantidaddías= -1
        D= D + 1
    if  D>cantidaddías:
        D= 1
        M= M + 1
        A= A + 1
    n= n + 1
        
print("Fecha", D/M/A)

#6.
n= int(input("Ingresar número entero"))
num=n
if n<0:
    num= num*(-1)
    
cant=0
while n>0:
    división= n//10
    cant= cant+1
    n= división
    
print("El número", num, "tiene", cant, "dígitos.")

#7.
num = int(input("Ingrese un número: "))
if (num < 0):
    num = (num * (-1))

c_4 = (num % 10)
c_3 = ((num // 10) % 10)
c_2 = ((num // 100) % 10)
c_1 = ((num // 1000) % 10)

print(c_4,c_3,c_2,c_1)

#8.
cant=0
mas200mil=0
sueldos_1=0
sueldos_2=0
sueldos_3=0
total=0
categ_cMen50mil=0
legajo_mayor=0
mayor=0
menor=0

empleados=int(input("Ingrese cantidad de empleados: "))
while empleados<=0:
    empleados=int(input("Ingrese la cantidad de empleados (numero mayor a 0): "))    
while cant < empleados:
    legajo=int(input("Ingrese su legajo: "))
    categoria=int(input("Ingrese su categoria 1, 2 o 3 "))
    cant=cant +1
    salario=int(input("Ingrese su salario: "))            
    total=total+salario
    if cant == 1:
        mayor=salario
        menor=salario
        legajo_mayor= legajo
    if salario > mayor:
        mayor=salario
        legajo_mayor= legajo
    elif salario < menor:
        menor=salario        
    if salario >200000:
        mas200mil=mas200mil+1 
    if categoria == 1:
        sueldos_1= sueldos_1 + salario
    elif categoria== 2:
        sueldos_2= sueldos_2 + salario
    elif categoria == 3:
        sueldos_3= sueldos_3 + salario
        if salario <50000:
            categ_cMen50mil= categ_cMen50mil +1 
#Imprimir                                     
print("Importe total de salarios pagados por la empresa:", total)
print("Salario promedio:", total/cant)
print("Cantidad de empleados que ganan más de $200000:",mas200mil )
print("Cantidad de empleados que ganan menos de $50000, cuya categoría sea 3:", categ_cMen50mil)
print("Sueldo más bajo:", menor)
print("El total de sueldos categoria 1: ",sueldos_1, ",el total de sueldos categoria 2: ",sueldos_2, " y el total de sueldos categoria 3: ",sueldos_3)    
print("Legajo del empleado que más gana, es: ", legajo_mayor)

#9.
N = int(input("Ingrese un número: "))
i = 1
suma_imp = 0
while(N < 0):
    print("Ingrese un número positivo")
    N = int(input("Ingrese un número: "))
if (N > 0):
    while (i <= N):
        if (i % 2 != 0):
            print(i)
            suma_imp = suma_imp + i
        i = i + 1
    print("La suma de los número impares comprendidos en N es:",suma_imp)