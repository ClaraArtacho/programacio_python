#RO_Pag071_exerci_2_area_triangle.py


from math import*

print("Introdueix el valor de la diagonal: ",end="")
d = float(input())

print("Introdueix el valor de l'angle: ", end="")
alfa = float(input())

alfa = alfa * (pi/180) #pas a radiants

altura = d * sin(alfa)
base = d * cos(alfa)

area = (altura * base)/2
print("Area del triangle = ", area)