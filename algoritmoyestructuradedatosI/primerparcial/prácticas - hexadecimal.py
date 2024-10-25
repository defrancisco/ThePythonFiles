"""El sistema de numeración hexadecimal es un sistema de representación numérica que utiliza 16 dígitos distintos en lugar de los 10 usados habitualmente en el sistema decimal.
Por esa razón luego del 9 se agregan las letras de la A a la F.
Para convertir un número decimal a hexadecimal basta con dividir repetidamente al número sobre 16 y tomar los restos obtenidos en orden inverso.

Ejemplo: 300dec => 12Chex

300 |__16__
 18   |__16__
  1    |__16__
  0

Escribir un programa que utilice una función para convertir un número decimal en su equivalente hexadecimal.
Tener en cuenta que la función recibe un número entero y devuelve una cadena de caracteres.
"""
def decimal_a_hexadecimal(decimal):
    # Definir los dígitos hexadecimales
    digitos_hexadecimales = "0123456789ABCDEF"
    resultado = ""

    # Convertir el número decimal a hexadecimal
    while decimal > 0:
        resto = decimal % 16
        resultado = digitos_hexadecimales[resto] + resultado
        decimal //= 16

    return resultado

# Programa principal
numero_decimal = int(input("Ingrese un número decimal: "))
hexadecimal = decimal_a_hexadecimal(numero_decimal)
print(f"El número decimal {numero_decimal} en hexadecimal es: {hexadecimal}")
