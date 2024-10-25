def reemplazarvocales(lista):
    contilde = "áéíóú"
    sintilde = "aeiou"
    for i in range(len(lista)):
        if lista[i] in contilde:
            lista[i] = sintilde[contilde.index(lista[i])]

def esanagrama(fr1, fr2):
    fr1 = fr1.lower()
    fr2 = fr2.lower()
    # Chequeamos que sean solo letras 
    lista1 = [letra for letra in fr1 if letra.isalpha()]
    lista2 = [letra for letra in fr2 if letra.isalpha()]
    
    reemplazarvocales(lista1)
    reemplazarvocales(lista2)
    
    lista1.sort()
    lista2.sort()
    # Si luego de ordenar ambas listas, éstas resultan iguales, entonces son anagramas
    return lista1==lista2

# Programa principal
frase1 = input("Ingresá la primera frase: ")
frase2 = input("Ingresá la segunda frase: ")
print()
if esanagrama(frase1, frase2):
    print(f"{frase1} y {frase2} son anagramas")
else:
    print("No son anagramas")
        