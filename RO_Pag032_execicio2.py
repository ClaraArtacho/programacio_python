#RO_Pag032_execicio2.py

kwh = float(input("kwh = "))
preu_kwh = 0.335

if kwh > 700:
    preutotal = 1.05 * (1 * kwh) * preu_kwh
    
if kwh < 700:
    preutotal = (1 * kwh) * preu_kwh
    
print("preutotal = ", preutotal)
