"""Suma de los primeros digitos de cada n almacena en lista de enteros"""

def sumaprimerdigito(lista):
    suma_primeros= 0
    for nro in lista:
        primer_digito = int(str(nro)[0])
        # primer_digito = nro // 10 ** (len(str(nro)) - 1)
        suma_primeros += primer_digito
    return suma_primeros

#programa principal
lista = [1224,2345,354]
respuesta = sumaprimerdigito(lista)
print(respuesta)