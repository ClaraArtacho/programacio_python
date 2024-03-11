#RO_Pag096_exercici_7.py

from math import*

print("Introdueix el valor de t: ", end= "")
t = float(input())

print("Introdueix el valor de p: ", end= "")
p = float(input())

if p == 1:
    c = 5/9 * (t-32)
    print("Introdueix la temperatura en graus centígrads = ",c)
    
if p == 2:
    f = 32 + ((9 * t) / 5)
    print("Introdueix la temperatura en graus farenheids = ",f)

else:
    print("Error")


