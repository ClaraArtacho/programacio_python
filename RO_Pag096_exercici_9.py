#RO_Pag096_exercici_9.py

from math import*

print("Introdueix el valor de nota 1: ", end= "")
nota1 = float(input())

print("Introdueix el valor de nota 2: ", end= "")
nota2 = float(input())

print("Introdueix el valor de nota 3: ", end= "")
nota3 = float(input())

if nota1 == nota2 and nota2 == nota3:
    print("Totes les notes són iguals: ", nota1, nota2, nota3)
elif nota1 == nota2:
    if nota1 > nota3:
        print("Les notes 1 i 2 són les més grans: ", nota1, nota2)
    else:
        print("La nota 3 és la més gran: ", nota3)
elif nota3 == nota2:
    if nota3 > nota1:
        print("Les notes 3 i 2 són les més grans: ", nota3, nota_2)
    else:
        print("La nota 1 és la més gran: ", nota1)
elif nota1 == nota3:
    if nota1 > nota2:
        print("Les notes 1 i 3 són les més grans: ", nota1, nota3)
    else:
        print("La nota 2 és la més gran: ", nota2)
elif nota1 > nota2 and nota1 > nota3:
    print("Valor de la nota 1 es la mes gran = ", nota1)
elif nota2 > nota1 and nota2 > nota3:
    print("Valor de la nota 2 es la mes gran = ", nota2)
else:
    print("Valor de la nota 3 es la mes gran = ", nota3) 
elif nota1 == nota2:
    if nota1 < nota3:
        print("Les notes 1 i 2 són les més petites: ", nota1, nota2)
    else:
        print("La nota 3 és la més petita: ", nota3)
elif nota3 == nota2:
    if nota3 < nota1:
        print("Les notes 3 i 2 són les més petites: ", nota3, nota2)
    else:
        print("La nota 1 és la més petita: ", nota1)
elif nota1 == nota3:
    if nota1 < nota2:
        print("Les notes 1 i 3 són les més petites: ", nota1, nota3)
    else:
        print("La nota 2 és la més petita: ", nota2)
    
elif nota_1 < nota_2 and nota_1 < nota_3:
    print("Valor de la nota 1 es la mes petita = ", nota_1)
elif nota_2 < nota_1 and nota_2 < nota_3:
    print("Valor de la nota 2 es la mes petita = ", nota_2)
else:
    print("Valor de la nota 3 es la mes petita = ", nota_3)
