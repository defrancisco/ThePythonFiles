def suma_recursiva(n):
    if n == 0:      # Caso base
        return 0
    else:
        return n + suma_recursiva(n-1)  # Llamada recursiva

# Solicitar al usuario un número
numero = int(input("Ingrese un número entre 5 y 10 para calcular la suma de los números naturales hasta ese número: "))

# Verificar si el número está en el rango correcto
if 5 <= numero <= 10:
print(f"La suma de los números naturales hasta {numero} es {suma_recursiva(numero)}")
else:
    print("El número ingresado no está en el rango de 5 a 10.")
