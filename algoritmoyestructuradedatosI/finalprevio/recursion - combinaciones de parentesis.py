'''
Ejercicio: Generar todas las combinaciones posibles de paréntesis balanceados

El objetivo de este ejercicio es escribir una función recursiva que genere todas las combinaciones posibles de paréntesis
balanceados para un número dado de pares de paréntesis.
Por ejemplo, si el número es 2, las combinaciones posibles serían ["(())", "()()"]
'''

def generarparentesis(pares, combinacion = '', abierto = 0, cerrado = 0):
    if abierto == pares and cerrado == pares:
        print(combinacion)
    else:
        if abierto < pares:
            generarparentesis(pares, combinacion + '(', abierto +1, cerrado)
        if cerrado < abierto:
            generarparentesis(pares, combinacion + ')', abierto, cerrado+1)
        
#programa principal
numero_pares = int(input("Ingrese el número de pares de paréntesis: "))
generarparentesis(numero_pares)