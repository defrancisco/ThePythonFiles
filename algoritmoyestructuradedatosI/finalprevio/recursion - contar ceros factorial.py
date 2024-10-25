'''determina la cantidad de ceros al final
de la representación factorial de un número entero'''

def contarcerosfactorial(n):
    if n == 0:
        return 0
    else:
        ceros = n//5
        return ceros + contarcerosfactorial(n // 5)
    
    
    
    
"""

La razón por la cual se utiliza el número 5 para contar los ceros al final de un factorial es debido a que los ceros son el resultado de multiplicar factores de 10, y un 10 se forma con un 2 y un 5 multiplicados. Como en los factoriales hay más factores de 2 que de 5, el número de ceros está determinado por la cantidad de veces que el número 5 aparece como factor en la descomposición en factores primos de todos los números del factorial.

Por ejemplo, en \( 10! \), que es \( 10 \times 9 \times 8 \times 7 \times 6 \times 5 \times 4 \times 3 \times 2 \times 1 \), hay dos cincos (uno en el 5 y otro en el 10), y más que suficientes doses para combinar con esos cincos para hacer dos dieces, o lo que es lo mismo, dos ceros al final de \( 10! \).

Por lo tanto, para contar la cantidad de ceros al final de un factorial, solo necesitamos contar cuántos múltiplos de 5 hay en la secuencia de números que forman el factorial, y para números más grandes, cuántos múltiplos de \( 5^2 \), \( 5^3 \), etc., porque estos contribuirán con ceros adicionales.

Espero que esta explicación te haya ayudado a entender mejor el proceso. Si tienes más preguntas o necesitas más ejercicios, estaré encantado de ayudarte. ¿Hay algo más en lo que pueda asistirte?
"""