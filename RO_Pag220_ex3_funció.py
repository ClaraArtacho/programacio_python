#RO_Pag220_ex3_funció.py

def vectmax(v):
    n = len(v)
    r = v[0]
    p = 0
    for i in range(1,n):
        if v[i]>r:
            r = v[i]
            p = i
    return(r,p)

x=[11, 5, 18, 16, 14, 11, 13, 3, 18, 16]
[r,p] = vectmax(x)
print(r)
print(p)


