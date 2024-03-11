#RO_Pag095_exercici_4.py

from math import*

print("Introdueix el valor de n: ", end= "")
n = float(input())

a = n % 10
b = n // 10

c = a + b

if c % 2 == 0:
    print("Par: ", c)
else:
    print("Impar: ", c)


