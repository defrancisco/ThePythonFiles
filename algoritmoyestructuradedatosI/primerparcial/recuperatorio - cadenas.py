"""Ordenar una lista de direcciones IP en función de los primeros tres números de cada dirección"""

def sacarlostresprimerosdigitos(num):
    if num <10: # tiene un solo digito
        return "00" + str(num)
    elif num < 100: #tiene dos digitos
        return "0" + str(num)
    else:
        return str(num)

def customcompare(ip):
    numeros = ip.split(".")  # Divide la dirección IP en una lista de subcadenas cada vez que encuentra un punto "."
    primeros_numeros = ".".join(  # Une los tres primeros números de la dirección IP con al menos tres dígitos cada uno
        sacarlostresprimerosdigitos(int(num))  # Llama a la función sacarlostresprimerosdigitos() para cada número
        for num in numeros[:3]  # Itera sobre los primeros tres números de la lista de la dirección IP
    )
    return primeros_numeros


# Programa principal
# Lista de direcciones IP para ordenar (con dos o tres números al principio)
ip_list = [
    "191.1245.12",
    "23.5635.265",
    "191.1245.12.1",
    "23.5635.265.0",
    "1.1.1",
    "192.168.0.1",
    "10.0.0.1",
    "172.16.0.1",
    "192.168.1.100",
    "10.0.0.2",
    "172.16.0.2",
    "200.5.4.3",
    "200.5.4.30",
    "200.5.4.300",]

ip_list.sort(key= customcompare)
print(ip_list)