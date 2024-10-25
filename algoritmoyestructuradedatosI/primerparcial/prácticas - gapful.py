"""Gapful Number es un número N de al menos 3 dígitos
tal que es divisible por la concatenación de su primer y
último dígito."""

def esgapful():
    N = int(input("Ingrese el nro a verificar: "))
    es_gapful = True
    if N <100:
        es_gapful = False
        print("Tiene al menos tres dígitos")
    concatenación = int( str(N)[0] + str(N)[-1])
    if N % concatenación != 0:
        es_gapful = False
    return es_gapful
    
    
    
    
#programa principal
print("Números Gapful")
print()
respuesta = esgapful()
if respuesta:
    print("¡El número", respuesta, "es un número Gapful!")
else:
    print("El número", respuesta, "no es un número Gapful.")