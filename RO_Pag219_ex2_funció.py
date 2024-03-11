#RO_Pag219_ex2_funció.py

def norep(v):
    u = []
    for e in v:
        if e not in u:
            u.append(e)
    return u

v = []
n = int(input("Introdueix la quantit de num: "))

for i in range(n):
    x = int(input("Introdueix un num: "))
    v.append(x)
    
print(norep(v))

