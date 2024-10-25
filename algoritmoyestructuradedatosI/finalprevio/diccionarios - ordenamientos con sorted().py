
cantidad = {'Cpalabra1': 4, 'Apalabra2': 2, 'Bpalabra3': 3}

# Ordenar por valor en orden ascendente
ordenado_por_valor = {k: v for k, v in sorted(cantidad.items(), key=lambda x: x[1])}
print(ordenado_por_valor)

# Ordenar por valor en orden descendente
ordenado_por_valor_desc = {k: v for k, v in sorted(cantidad.items(), key=lambda x: x[1], reverse=True)}
print(ordenado_por_valor_desc)

# Ordenar por clave en orden alfabético
ordenado_por_clave = {k: v for k, v in sorted(cantidad.items())}
print(ordenado_por_clave)

# Ordenar por la longitud de la clave y luego por el valor en orden descendente
ordenado_por_longitud_y_valor = {k: v for k, v in sorted(cantidad.items(), key=lambda x: (len(x[0]), -x[1]))}
print(ordenado_por_longitud_y_valor)
