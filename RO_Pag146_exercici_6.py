#RO_Pag146_exercici_6.py


n = int(input("Introduir el valor de n = "))
a = 0
b = 0
c = 0
v_blanc = 0
nulo = 0

comptador = 0

while comptador < n:
    voto = int(input("Introdueix el vot: "))
    
    if voto == 1:
        a = a + 1
    elif voto == 2:
        b = b + 1
    elif voto == 3:
        c = c + 1
    elif voto == 0:
        v_blanc = v_blanc + 1
    else:
        nulo = nulo + 1
    
    comptador = comptador + 1
        
print("A = ", a)
print("B = ", b)
print("C = ", c)
print("v_blanc = ", v_blanc)
print("nulo = ", nulo)
