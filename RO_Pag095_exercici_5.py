#RO_Pag095_exercici_5.py

from math import*

print("Introdueix el valor de n: ", end= "")
n = float(input())

if n == int(n):
    print("numero enter = ", n)
    
    if n%7 == 0:
        print("multiple de 7")
        
else:
    print("Error")
    