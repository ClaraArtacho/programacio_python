#RO_Pag071_exercici_5_b.py


from math import*

print("Introdueix el valor de a: ", end= "")
a = int(input())

print("Introdueix el valor de x: ", end= "")
x = float(input())

print("Introdueix el valor de n: ", end= "")
n = float(input())
n = n * 20

p = a/((((1 + x) ** n) - 1)/x)

print("valor de cada depòsito mensual = ", p)