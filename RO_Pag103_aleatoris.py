#RO_Pag103_aleatoris.py

from random import*

c = 0
x = 0

while x != 3:
    x = randint(1,6)
    print(x)
    c = c + 1
print("Cantidad de lanzamientos hasta que salga el 3 = ", c)
