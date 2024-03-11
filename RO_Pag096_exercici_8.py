#RO_Pag096_exercici_8.py

from math import*

print("Introdueix el valor de nota1_1: ", end= "")
nota1_1 = float(input())

print("Introdueix el valor de nota1_3: ", end= "")
nota1_2 = float(input())

print("Introdueix el valor de nota1_2: ", end= "")
nota1_3 = float(input())

print("Introdueix el valor de nota2_1: ", end= "")
nota2_1 = float(input())

print("Introdueix el valor de nota2_2: ", end= "")
nota2_2 = float(input())

print("Introdueix el valor de nota2_3: ", end= "")
nota2_3 = float(input())


nota_1 = (nota11 + nota12) / 2
nota_2 = (nota2_1 + nota2_2) / 2



if nota_1 > nota_2:
    print("La nota del  estudiant 1 és la més alta = ", nota_1)

else:
    print("La nota del  estudiant 2 és la més alta = ", nota_2)

