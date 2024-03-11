#RO_Pag180_exercici_1.py

def conteo(n):
    contador = 0
    for i in range(1, n + 1):
        if n % i == 0:
            contador = contador + 1
    return contador

numero_de_divisors = 0
numero_amb_maxim_divisors = 0

for n in range(1, 101):
    divisors = conteo(n)
    print (divisors)
    if divisors > numero_de_divisors:
        numero_de_divisors = divisors
        numero_amb_maxim_divisors = n

print("El número amb més divisors entre 1 y 100 es: ", numero_amb_maxim_divisors)
print("El número de divisors es: ", numero_de_divisors)
