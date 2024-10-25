#2.
a= int(input("Ingresar un número entero:"))
b= int(input("Ingresar otro número entero:"))

suma= a + b
diferencia= a - b

print("La suma de", a, "con", b , "es", suma)
print("La diferencia de", a ,"con", b, "es",  diferencia)

#3
nota1= float(input("Ingresar primer parcial:"))
nota2= float(input("Ingresar segundo parcial:"))

promedio= nota1 + nota2 

print("El promedio del alumno es de", promedio/2)

#4
años= int(input("Ingresar edad en años:"))
días=365
a= años * días

print(a,"días.")

#5 PRESTAR ATENCIÓN AL PROMEDIO CANTIDAD*100/TOTAL
p1= int(input("Ingresar monto"))
p2= int(input("Ingresar monto"))
p3= int(input("Ingresar monto"))

total= p1 + p2 + p3

print("Persona 1 invirtió", p1*100/total)
print("Persona 2 invirtió", p2*100/total)
print("Persona 3 invirtió", p3*100/total)

# 6. Ingresar tres números enteros, calcular su promedio y mostrarlo por pantalla.
a = int(input("Ingresar número entero:"))
b = int(input("Ingresar número entero:"))
c = int(input("Ingresar número entero:"))

print(int(a + b + c) / 3)

#7
capital=int(input("Ingresar capital:"))
ganacia= capital * .02 #recordar que 2% se escribe .02

print("En seis meses dejando su dinero invertido ganará", ganacia*6)

#8
metros= int(input("Ingresar medida en metros "))

centimetros= metros *100
pulgadas= centimetros/2.54
pies= pulgadas/ 12
yarda= pies/3

print("Cemtimetros ", centimetros)
print("Pulgadas ", pulgadas)
print("Pies ", pies)
print("Yardas ", yarda)

#9
salario=50000
venta= 5000
valor= .05

nro= int(input("Ingresar número del vendedor "))
cv= int(input("Ingresar cantidad de ventas "))
vv= int(input("Ingresar valor de ventas "))

mes= salario + venta* cv + valor * vv


print("Número de vendedor ", nro)
print("Salario del mes", mes )

#10.
segundos= int(input("Ingresar período en segundos "))

minutos= segundos/60
horas= minutos/60
días= horas/24

print(días, "días")
print(horas, "horas")
print(minutos, "minutos")

#11.
dinero=int (input("Ingrese la cantidad de dinero a retirar: "))
bmil=dinero//1000
dinero=dinero%1000
bqui=dinero//500
dinero=dinero%500
bcien=dinero//100
dinero=dinero%100
bcin=dinero//50
dinero=dinero%50
bdiez=dinero//10
dinero=dinero%10

print("El cajero entregara ")
print(bmil," billetes de mil ")
print(bqui," billetes de quinientos")
print(bcien," billetes de cien ")
print(bcin," billetes de cincuenta")
print(bdiez,"monedas de diez")
print(dinero,"monedas de uno")

#12.
num=input ("ingrese un numero binario de 4 cifras:")
num = int (num)
num1 = num // 1000
resto_num1= num % 1000
num2= resto_num1 // 100
resto_num2= resto_num1 % 100 
num3= resto_num2 // 10   
resto_num3 = resto_num2 % 10   
num4= resto_num3

cifra4= num4 * (2 **0)
cifra3= num3 * (2 **1)
cifra2= num2 * (2 **2)
cifra1= num1 * (2 **3) 

total = cifra1 + cifra2 + cifra3 + cifra4
print()
print ("el numero ingresado es", total, "en sistema decimal")