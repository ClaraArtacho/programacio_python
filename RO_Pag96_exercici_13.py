#RO_Pag96_exercici_13.py

from math import*

print("Introdueix el valor de joan hores treballades: ", end= "")
j_h = float(input())

print("Introdueix el valor de joan salario por hora: ", end= "")
j_s = float(input())

print("Introdueix el valor de joan descuentos(%): ", end= "")
j_d = float(input())

print("Introdueix el valor de pedro hores treballades: ", end= "")
p_h = float(input())

print("Introdueix el valor de pedro salario por hora: ", end= "")
p_s = float(input())

print("Introdueix el valor de pedro descuentos(%): ", end= "")
p_d = float(input())

print("Introdueix el valor de emilio hores treballades: ", end= "")
e_h = float(input())

print("Introdueix el valor de emilio salario por hora: ", end= "")
e_s = float(input())

print("Introdueix el valor de emilio descuentos(%): ", end= "")
e_d = float(input())

j_ps = (j_h * j_s) / (100 - j_d)
print("Pago semanal Joan = ", j_ps)
p_ps = (p_h * p_s) / (100 - p_d)
print("Pago semanal Pedro = ", p_ps)
e_ps = (e_h * e_s) / (100 - e_d)
print("Pago semanal Emilio = ", e_ps)

if j_ps > p_ps:
    if j_ps > e_ps:
        print("Juan tiene el mayor pago semanal")
    else:
        print("Emilio tiene el mayor pago semanal")
elif p_ps > j_ps:
    if p_ps > e_ps:
        print("Pedro tiene el mayor pago semanal")
    else:
        print("Emilio tiene el mayor pago semanal")
else:
    print("Emilio tiene el mayor pago semanal")



