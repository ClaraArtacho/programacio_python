#RO_Pag025_diametre.py

h = float(input("h =",)) #altura
volum = float(input("volum =")) #volum
pi = 3.1416

volum = volum / 1000
diametre = ((volum * 4)/(pi * h))**0.5

print("diametre =", diametre)

