
#RO_Pag218_ex2_llista.py

n = int(input("Introdueix quatitat de numeros: "))
v = []

for i in range(n):
    x = int(input("Introdueix el nuemro: "))
    v.append(x)
print(v)

u = []
for e in v:
    if e not in u:
        u.append(e)
print(u)