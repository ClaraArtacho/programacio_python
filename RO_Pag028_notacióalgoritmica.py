#RO_Pag028_notacióalgoritmica.py

n = float(input("n = ")) #cantidad llantas
p = float(input("p = ")) #precio inicial cada llanta

if n > 4 :
    t = 0.9 * (p * n)
if n < 4 :
    t = n * p

print("t = ", t) #valor a pagar
