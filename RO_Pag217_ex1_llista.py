#RO_Pag217_ex1_llista.py

n = int(input("Introdueix quatitat de numeros: "))
v = []

for i in range(n):
    x = int(input("Introdueix el nuemro: "))
    v.append(x)
    
s = 0

for e in v:
    if e%2 == 0:
        s = s + e
        
print(s)
    
    