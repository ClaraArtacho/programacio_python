#RO_Pag096_exercici_6

from math import*

print("Introdueix el valor de cantidad Kw: ", end= "")
cantidad = float(input())

preu_Kw = 0.3321 

if cantidad > 700:
    preu = (preu_Kw * cantidad) * 1.05
    print("Preu en total a pagar = ", preu)
else:
    preu = (preu_Kw * cantidad)
    print("Preu en total a pagar = ", preu)
