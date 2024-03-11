#RO_Pag217_ex1_funció.py

def sumap(v):
    s = 0
    for e in v:
        if e%2 == 0:
            s = s + e
    return s
v = []
n = int(input("Introdueix la quantitat de num: "))
for i in range(n):
    x = int(input("Introdueix un num: "))
    v.append(x)
    
print(sumap(v))
        