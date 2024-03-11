#RO_Pag104_suma_quadrats.py


n = int(input("Ingrese el valor final: "))
s = 0
i = 1

while i <= n:
    c = i ** 2
    s = s + c
    i = i + 1
    
print('La suma es: ', s)