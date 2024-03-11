#RO_Pag032_execicio3.py

t = float(input("t = ")) #temperatura
p = float(input("p = ")) #codigo

if p == 1:
    c = 5 / 9 * (t - 32)
    print("c = ", c)

if p == 2:
    f = 32 + 9 * (t / 5)
    print("f = ", f)