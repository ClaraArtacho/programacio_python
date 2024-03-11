#RO_Pag097_exercici_19.py

from math import*

print("Introdueix el valor de j1: ", end= "")
j1 = float(input())

print("Introdueix el valor de j2: ", end= "")
j2 = float(input())

print("Introdueix el valor de j3: ", end= "")
j3 = float(input())


if j1 == "0" and j2 == "1" and j3 == "1": #011
    print("Coninua")
elif j1 == "1" and j2 == "0" and j3 == "1": #101
    print("Continua")
elif j1 == "1" and j2 == "1" and j3 == "0": #110
    print("Continua")
elif j1 == "1" and j2 == "1" and j3 == "1": #111
    print("Continua")
else:
    j1 == "0" and j2 == "0" and j3 == "0"
    print("Elimina") #000