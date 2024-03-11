#RO_Pag032_execicio4.py

a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

cara_1 = ((a * a) + (b * b)) ** 0.5
cara_2 = ((a * a) + (c * c)) ** 0.5
cara_3 = ((b * b) + (c * c)) ** 0.5

print("car+llarga = ", max(cara_1, cara_2, cara_3))




