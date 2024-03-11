#RO_Pag149_exercici_35.py

a = int(input("Introdueix a entre 1 i 1000: "))
b = int(input("Introdueix b entre 1 i 1000: "))

for a in range (a, a+1):
    for b in range (b, b+1):
        x = 1000 - a
        y = 1000 - b
        suma = x + y
        resta = 1000 - suma
        producte_1 = resta * 1000
        producte_2 = x * y
        resultat = producte_1 + producte_2
        
        