#RO_Pag096_exemple_11.py


from math import*

print("Introdueix el valor de abscisa punt 1: ", end= "")
a = float(input())

print("Introdueix el valor de ordenades punt 1: ", end= "")
b = float(input())

print("Introdueix el valor de abscisa punt 2: ", end= "")
c = float(input())

print("Introdueix el valor de ordenades punt 2: ", end= "")
d = float(input())

x = sqrt(pow(a, 2) + pow(b, 2)) #x = (a, b)
y = sqrt(pow(c, 2) + pow(d, 2)) #y = (c, d)

if x == y:
    print("Punt 1 i Punt 2")
elif x > y:
    print("Punt 1")
else:
    print("Punt 2")

