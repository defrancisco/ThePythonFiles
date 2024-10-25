def es_palindromo(cadena):
    # Caso base: si la cadena tiene 0 o 1 caracteres, es un palíndromo
    if len(cadena) <= 1:
        return True
    # Caso recursivo: compara el primer y último carácter y llama recursivamente con la cadena restante
    elif cadena[0] == cadena[-1]:
        return es_palindromo(cadena[1:-1])  # Se llama recursivamente con la cadena excluyendo el primer y último carácter
    else:
        return False

# Ejemplo de uso
cadena1 = "anita lava la tina"
cadena2 = "python"
if es_palindromo(cadena1):
    print(f'"{cadena1}" es un palíndromo.')
else:
    print(f'"{cadena1}" no es un palíndromo.')

if es_palindromo(cadena2):
    print(f'"{cadena2}" es un palíndromo.')
else:
    print(f'"{cadena2}" no es un palíndromo.')
