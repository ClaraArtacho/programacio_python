#RO_Pag081_exercici_9.py

from math import*

print("Introdueix el valor de a: ", end= "")
a = float(input())

print("Introdueix el valor de b: ", end= "")
b = float(input())

print("Introdueix el valor de c: ", end= "")
c = float(input())

print("Introdueix el valor de d: ", end= "")
d = float(input())


x = sqrt(pow((c - a), 2) + pow((d - b), 2))
print("distancia de P a Q: ", x)

y = sqrt(pow(a, 2) + pow(b, 2))
print("distancia de P a O: ", y)

z = sqrt(pow(c, 2) + pow(d, 2))
print("distancia de Q a O: ", z)

t = (x + y + z)/2

A = sqrt(t * (t - x) * (t - y) * (t - z))
print("Area del triangle = ", A)

