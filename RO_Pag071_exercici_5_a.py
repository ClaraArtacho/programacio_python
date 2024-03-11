#RO_Pag071_exercici_5_a.py

from math import*

print("Introdueix el valor de p: ", end= "")
p = float(input())

print("Introdueix el valor de x: ", end= "")
x = float(input())

print("Introdueix el valor de n: ", end= "")
n = int(input())

a = p * ((((1 + x) ** n) - 1)/x)


print("valor acumulado = ", a)