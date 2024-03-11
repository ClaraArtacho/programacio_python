#RO_Pag041_exercici_01_pespaquets_amb_while

n_paquets = 1
pes_maxim = 0

while n_paquets != 10:
    print("pes_paquet" ,n_paquets, "en kg = " , end = " ")
    pes_paquet = float(input())
    if pes_paquet > pes_maxim :
        pes_maxim = pes_paquet
    n_paquets = n_paquets + 1
print("el paquet més grann val:" , pes_maxim)
    
    