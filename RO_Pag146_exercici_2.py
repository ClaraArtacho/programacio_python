#RO_Pag146_exercici_2.py

n = int(input("Introdueix num. de objecte: "))

comptador = 0
menor_10kg = 0
entre_10kg_i_20kg = 0
mayor_20kg = 0

while n > comptador:
    pes = float(input("Introdueix el pes: " + str(comptador + 1) + ":"))
    
    if pes < 10:
        menor_10kg += 1
    elif pes > 10 and pes < 20:
        entre_10kg_i_20kg += 1
    else:
        mayor_20kg += 1
        
    comptador = comptador + 1
    
    
print("Numero de objectes menors de 10kg = ", menor_10kg)
print("Numero de objectes entre 10kg i 20kg = ", entre_10kg_i_20kg)
print("Numero de objectes majors de 20kg = ", mayor_20kg)