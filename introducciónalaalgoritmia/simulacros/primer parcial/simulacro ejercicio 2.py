nro=int(input("Ingrese un valor "))
nrot=nro
if nro<0:
    nro=nro*(-1)
cant=0
while nro>0:
    div=nro//10
    cant=cant+1
    nro=div
print ("el numero",nrot,"tiene",cant,"digitos")
    