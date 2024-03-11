#RO_Pag083_exercici_1

from math import*

print("Introdueix el valor de dies: ", end= "")
dies = int(input())

anys = dies // 365

dies_restants = dies % 365

setmanes_restants = dies_restants // 7

dies_restants_1 = dies_restants % 7

print("Anys = ", anys)
print("Setmanes = ", setmanes_restants)
print("Dies = ", dies_restants_1)



