#RO_Pag095_exercici_3.py

from math import*

print("Introdueix el valor de altura: ", end= "")
altura = float(input())

print("Introdueix el valor de base: ", end= "")
base = float(input())

print("Introdueix el valor de profunditat: ", end= "")
profunditat = float(input())

d1 = sqrt(pow(base,2) + pow(altura,2))
d2 = sqrt(pow(base,2) + pow(profunditat,2))
d3 = sqrt(pow(profunditat,2) + pow(altura,2))

if d1 == d2 and d2 == d3:
    print("Totes les diagonals són iguals: ", d1, d2, d3)
elif d1 == d2:
    if d1 > d3:
        print("Les diagonals 1 i 2 són les més grans: ", d1, d2)
    else:
        print("La diagonal 3 és la més gran: ", d3)
elif d3 == d2:
    if d3 > d1:
        print("Les diagonals 3 i 2 són les més grans: ", d3, d2)
    else:
        print("La diagonal 1 és la més gran: ", d1)
elif d1 == d3:
    if d1 > d2:
        print("Les diagonals 1 i 3 són les més grans: ", d1, d3)
    else:
        print("La diagonal 2 és la més gran: ", d2)
elif d1 > d2 and d1 > d3:
    print("Valor de la diagonal 1 es la mes gran = ", d1)
elif d2 > d1 and d2 > d3:
    print("Valor de la diagonal 2 es la mes gran = ", d2)
else:
    print("Valor de la diagonal 3 es la mes gran = ", d3)

        

        