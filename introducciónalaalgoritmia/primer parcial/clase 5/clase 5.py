# ejemplo 1 : cálculo de un promedio
# función
def calcularpromedio (a,b):
    total = (a + b)/2 #parámetros formales a y b
    return total

#programa principal
x = int(input("Ingrese un número entero:"))
y = int(input("Ingrese otro número entero:"))
resultado= calcularpromedio(x,y) # parámetros reales x e y
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

# Escribir una función para ingresar un número entero a través del teclado, verificando que éste se encuentre dentro de los límites permitidos.
def leerentero (minimo, máximo):
    print("Ingrese un número entero entere", minimo, "y", máximo, ":")
    a = int(input()) #¿por qué el msj no se muestra aquí
    
    while a<minimo or a>máximo:
        print("Valor incorrecto.")
        print("Debe estar entre", minimo, "y", máximo)
        a = int(input("Ingrese un número entero:"))
    return a