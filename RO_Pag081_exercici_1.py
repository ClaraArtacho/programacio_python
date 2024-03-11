#RO_Pag081_exercici_1.py

from math import*

print("Introdueix el valor de el radi: ", end= "")
radi = float(input())

print("Introdueix el valor de l'altura: ", end= "")
altura = float(input())

A = 2 * pi *radi * (radi + altura)

print("valor de l'area = ", A)

V = pi * pow(radi, 2) * altura

print("valor del volum = ", V)
