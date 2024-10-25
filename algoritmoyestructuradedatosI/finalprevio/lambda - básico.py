'''Nivel Básico:
1. Escribe una función lambda que devuelva el doble de un número.
2. Utiliza map() para aplicar la función lambda del punto 1 a una lista de números.
3. Escribe una función lambda que verifique si un número es par.
'''

# eje1
doblenum = lambda x: x * 2
print(f"El doble del número es {doblenum(3)}.")

# eje2
lista = [123, 35, 2, 467, 57, 98768]
listaconmap = list(map(doblenum, lista))
print(f"La lista original es: {lista}")
print(f"La lista con el doble de cada elemento es: {listaconmap}")

# eje3
es_par = lambda x: x % 2 == 0
print(f"El número 3 es par: {es_par(3)}")

'''Nivel Intermedio:
1. Escribe una función lambda que concatene dos cadenas de texto.
2. Utiliza map() para aplicar la función lambda del punto 4 a dos listas de cadenas de texto.
3. Escribe una función lambda que cuente la longitud de una cadena de texto.
'''

# eje1
concatenar = lambda x, y: x + y
print(f"Cadenas concatenadas: {concatenar('buenas', 'noches')}")

# eje2
lista1 = ["Previo", "Delfi"]
lista2 = ["Aprobado", "Feliz"]
print(f"Concatenación: {list(map(concatenar, lista1, lista2))}")

# eje3
largo = lambda x: len(x)
print(f"El largo de la cadena es: {largo('Hola')}.")

'''Nivel Difícil:
1. Escribe una función lambda que multiplique dos números y les sume uno.
2. Utiliza map() para aplicar la función lambda del punto 7 a dos listas de números.
3. Escribe una función lambda que calcule el área de un triángulo dados su base y altura.'''

# eje1
multiplicacionysuma = lambda x, y: (x * y) + 1

# eje2
lista1 = [2, 3, 4]
lista2 = [5, 6, 7]
listas = list(map(multiplicacionysuma, lista1, lista2))
print(f"Lista resultante: {listas}")

# eje3
calculararea = lambda base, altura: (base * altura) / 2

'''Nivel Complejo:
1. Escribe una función lambda que verifique si una palabra es un palíndromo.
3. Utiliza filter() para filtrar una lista de palabras y quedarte solo con los palíndromos utilizando la función lambda del punto 10.
3. Escribe una función lambda que reciba dos listas y devuelva una lista que contenga solo los elementos que están en ambas listas.
'''

# eje1
palindromo = lambda palabra: palabra.lower() == palabra.lower()[::-1]

# eje2
listapalindroma = ['radar', 'amar', 'reconocer', 'conocer']
espalindroma = list(filter(palindromo, listapalindroma))
print(f"Palíndromos: {espalindroma}")

# eje3
lista1 = [1, 2, 3, 4, 5]
lista2 = [4, 5, 6, 7, 8]
elementos_comunes = [x for x in lista1 if x in lista2]
print(f"Elementos comunes: {elementos_comunes}")
