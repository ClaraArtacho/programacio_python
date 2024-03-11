##RO_Pag032_execicio1.py

radi = float(input("radi = "))
altura = float(input("altura = "))
pi = 3.1415

if altura > radi:
    volum = altura * pi * radi * radi
    print("volum = ", volum)
    
if altura < radi:
    area = 2 * pi * radi * (radi + altura)
    print("area = ", area)

