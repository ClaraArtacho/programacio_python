#RO_Pag146_exercici_11.py

n = int(input("Ingrese el valor de n: "))

if n == 1:
    print("La suma de los primeros términos de la serie es: 1")
    
elif n == 2:
    print("La suma de los primeros términos de la serie es: 2")
else:
    a = 1
    b = 1  # dos primeros num.
    suma = a + b  # suma dels dos primers num.
    contador = 3  # Comencem desde el tercer num.
    
    while contador <= n:
        siguiente_termino = a + b
        suma = suma + siguiente_termino
        a, b = b, siguiente_termino
        contador = contador + 1

    print("La suma de los primeros términos de la serie es:", suma)
