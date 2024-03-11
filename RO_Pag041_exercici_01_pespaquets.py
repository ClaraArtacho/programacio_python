#RO_Pag041_exercici_01_pespaquets


num_paquets = 10
pes_maxim = 0

for comptador in range (1, num_paquets+1, 1):
    print("pes pquets ", comptador, " en kg = ", end = " ")
    pes_paquet = float(input())
    if pes_paquet > pes_maxim:
        pes_maxim = pes_paquet
           
print( "el pes del  paquet més gran val: ", pes_maxim)