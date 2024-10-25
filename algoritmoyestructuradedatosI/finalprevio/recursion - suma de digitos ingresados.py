def sumadigitos(n):
    if n== 0:
        return 0
    else:
        return n % 10 + sumadigitos(n//10)
    
    
# Solicitar al usuario un número
numero = int(input("Ingrese un número para calcular la suma de sus dígitos: "))

# Calcular y mostrar la suma de los dígitos
print(f"La suma de los dígitos de {numero} es {sumadigitos(numero)}")