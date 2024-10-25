"""Una Administradora de Consorcios necesita un sistema para poder gestionar el
cobro de las expensas de un edificio de departamentos de 20 unidades. En dos
listas almacena la siguiente información: Número de unidad y superficie en metros
cuadrados. Validar que no se ingresen números de unidades duplicadas. Cada
unidad paga de expensas un valor fijo por metro cuadrado, el que se ingresa
por teclado. Se pide:
· Informar el promedio de expensas del mes.
· Ordenar los listados de mayor a menor según la superficie. Mostrar por
pantalla el listado ordenado informando el número de unidad y la superficie
en metros cuadrados.""" """informar unidades con maxima recaudacion"""


def ordenar(lista1, lista2):
    for i in range (0, len(lista2)-1):
        for j in range (i+1, len(lista1)):
            if (lista2[j]<lista2[i]):
                aux=lista2[j]
                lista2[j]= lista2[i]
                lista2[i]=aux
                
                aux2=lista1[j]
                lista1[j]=lista1[i]
                lista1[i]=aux2
                
                
    

def buscar(lista, valor):
    pos=-1
    i=0
    while pos==-1 and i<len(lista):
        if lista[i]== valor:
            pos=i
        else:
            i+=1
    return pos

def promedio(uni, mts, valor):
    sumaExpensas =0
    for i in range (len(uni)):
        sumaExpensas += mts[i]*valor
    promedioExpensas = sumaExpensas / len(uni)
    
    print("las expensas promedio son " ,promedioExpensas)
        
        

def cargarListas(uni, mts):
    for i in range(4): #20 unidades
        unidad= int(input("ingrese numero de unidad: "))
        pos = buscar(uni, unidad)
        while pos>=0:
            unidad =int(input("error duplicado, ingrese nro de unidad "))
            pos = buscar(uni, unidad)
            
        metro= int(input("ingrese cantidad de metros "))
        uni.append(unidad)
        mts.append(metro)
    print(uni)
    print(mts)
        
            
   
def listar(uni, mts):
    for i in range(len(uni)):
        print("UNIDAD " ,uni[i], end= " ")
        print("METROS", mts[i])


#principal
unidades= [ ]
metros= [ ]


valorExpensa= float(input("ingrese el valor de expensas por metro cuadrados: "))
cargarListas(unidades, metros)

promedio(unidades, metros, valorExpensa)
ordenar(unidades, metros)

listar(unidades, metros)

