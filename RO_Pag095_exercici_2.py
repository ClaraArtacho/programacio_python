#RO_Pag095_exercici_2.py

from math import*

print("Introdueix el valor de radi: ", end= "")
radi = float(input())

print("Introdueix el valor de altura: ", end= "")
altura = float(input())

if altura > radi:
    V =  pi * altura * pow(radi,2)
    print("Volum = ", V)
else:
    if altura < radi:
        print("Error")