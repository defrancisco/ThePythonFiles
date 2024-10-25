def mcd_euclides(a, b):
    if b == 0:
        return a
    else:
        return mcd_euclides(b, a % b)

# Solicitar al usuario que ingrese dos números
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

# Calcular y mostrar el MCD
print(f"El máximo común divisor de {num1} y {num2} es {mcd_euclides(num1, num2)}")
