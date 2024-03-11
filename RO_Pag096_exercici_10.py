#RO_Pag096_exercici_10.py

from math import*

print("Introdueix el valor de lado1: ", end= "")
lado1 = float(input())

print("Introdueix el valor de lado2: ", end= "")
lado2 = float(input())

print("Introdueix el valor de lado3: ", end= "")
lado3 = float(input())

if lado1 == lado2 and lado1 == lado3:
    print("Es un triangulo equilater")
elif lado1 == lado2 and lado2 != lado3:
    print("Es un triangulo isosceles")
elif lado3 == lado2 and lado2 != lado1:
    print("Es un triangulo isosceles")
elif lado1 == lado3 and lado1 != lado2:
    print("Es un triangulo isosceles")
else:
    print("Es un triangulo escaleno")
    