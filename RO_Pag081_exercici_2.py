#RO_Pag081_exercici_2.py

from math import*

print("Introdueix el valor de l'altura: ", end= "")
altura = float(input())

print("Introdueix el valor del volum: ", end= "")
volum = float(input())
volum = volum / 1000

d = (altura * pi)/volum

print("valor del diametre = ", d)
