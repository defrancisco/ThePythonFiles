#1.
a= int(input("Ingresar número "))
b= int(input("Ingresar número "))

if a == b:
    print("son iguales")
else:
    print("son distintos")

#2.
n= int(input("Ingresar número "))

if n % 2 == 0:
    print("par")
else:
    print("impar")
    
#3.
nrom= int(input("Ingresar número de mes "))

if nrom == 1:
    print("ENERO")
elif nrom== 2:
    print("FEBRERO")
elif nrom== 3:
    print("MARZO")
elif nrom== 4:
    print("ABRIL")
elif nrom== 5:
    print("MAYO")
elif nrom== 6:
    print("JUNIO")
elif nrom== 7:
    print("JULIO")
elif nrom== 8:
    print("AGOSTO")
elif nrom== 9:
    print("SETIEMBRE")
elif nrom== 10:
    print("OCTUBRE")
elif nrom== 11:
    print("NOVIEMBRE")
elif nrom== 12:
    print("DICIEMBRE")
else:
    print("Ingresar número de mes válido")

#4.
n1= int(input("Ingresar nota de primer parcial "))
n2= int(input("Ingresar nota del segundo parcial "))

if (n1<1 or n2<1) and (n1>10 or n2>10):
    print("Ingresar números válidos")
elif n1 >=7 and n2 >=7:
    print("Promociona")
elif n1 >=4 and n2 >=4:
    print("Aprueba")
else:
    print("Debe recuperar")
    
#5.
npg= int(input("Ingresar número de páginas "))

básico= 500
perpágina= 3.20

if npg<=300:
    print("Costo es ", npg * perpágina + básico)
    print("Encuadernación rústica")
elif npg>300 and npg<=600:
    print("Costo es ", npg * perpágina + básico + 200)
    print("Encuadernación de tela")
elif npg>600:
    print("Costo es ", npg * perpágina + básico + 200 + 336)
    print("Especial")
    
#6.
    km = float(input("Ingresar cantidad de km que se desea recorrer "))
viajemin= 250

if km>=0 and km<10:
    print("El costo será", km*30)
elif km>=10:
    print("El costo será", km*20)
else:
    print("El costo será", viajemin)
    
#7.
año= int(input("Ingresar año "))
if año % 4 == 0 and  año % 100 == 0 and año % 400 == 0:
    print("Es bisiesto")
elif año % 4 == 0 and año % 100 == 0:
    print("No es bisisesto")

#8.
día= int(input("Ingresar día "))
mes = int(input("Ingresar mes "))
año = int(input("Ingresar año "))

if (día>=1 and día<=31) and (mes>=1 and mes<12) and (año>=1):
    print("Fecha válida")
else:
    print("Fecha inválida")

#9.
básico= int(input("Ingresar el suledo básico "))
ant= int(input("Ingresar antigüedad "))
esciv= int(input("Ingresar estado civil (1 si es soltero o 2 si es casado) "))

if esciv == 1:
    sueldo= (básico*5/100) * ant
if  esciv == 2:
    sueldo= (básico*7/100) * ant
else:
    print("error")
    
#DESCUENTOS
jub= básico*11/100
obs= básico*3/100
sind= básico*3/100
#SUELDO NETO
sueldoneto= básico+sueldo -(jub+obs+sind)

#PRINTS
print("Estado Civil:", esciv)
print("Sueldo básico               Antigüedad     Descuentos     Importe   ")
print(    básico,                     ant     ,                   básico    )
print("                             Jubilación     ",jub                    )
print("                             Obra Social    ",obs                    )
print("                             Sindicato      ",sind                   )
print("                                                         ----------" )
print("                             Sueld Neto                 ",sueldoneto )  
