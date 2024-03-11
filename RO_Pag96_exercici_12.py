#RO_Pag96_exercici_12.py

from math import*

print("Introdueix el valor de preu per article: ", end= "")
p_u = float(input())

print("Introdueix el valor de quantitat de productes: ", end= "")
c = float(input())

if c < 5:
    preu_total = p_u * c
    print("Preu total = ", preu_total)
elif c > 5 and c < 10:
    preu_total = (p_u / 1.05) * c
    print("Preu total = ", preu_total)
elif c >= 10:
    preu_total = (p_u / 1.08) * c
    print("Preu total = ", preu_total)
else:
    preu_total = p_u * c
    print("Preu total = ", preu_total)