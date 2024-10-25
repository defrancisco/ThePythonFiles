def invertircadena(cad):
    "con len"
    if len(cad) == 0:
        return  cadena
    else:
        return invertircadena(cad[1:]) + cad[0]
    
    
    
def longitudcadena(cad):
    if cad = "":
        return cad
    else:
        return 1 + longitudcadena(cad[1:])

def invertircadena2(cad,longitud):
    if longitud == 0:
        return ""
    else:
        return cad[longitud-1] + invertircadena2(cad,longitud-1)