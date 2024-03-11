#RO_Pag071_exercici_5_for_a

from math import*

print("Introdueix el valor de diposit mensual: ", end= "")
diposit_mensual= float(input())

print("Introdueix el valor de interes mensual: ", end= "")
interes_mensual= float(input())

print("Introdueix el valor de numero de diposits: ", end= "")
numero_de_diposits= int(input())

diners_dipositats = diposit_mensual + (interes_mensual * diposit_mensual)
for i in range(2, numero_de_diposits):
    mes_seguent = (diners_dipositats + diposit_mensual) + interes_mensual * (diners_dipositats + diposit_mensual)
    diners_dipositats = mes_seguent  

mes_seguent = (diners_dipositats + diposit_mensual)
print("diners totals = ", mes_seguent)