#RO_Pag148_exercici_24.py

from random import*
intents = 5
dollars = 0
n = 1

while n <= intents:
    numero = randint(1, 6)
    print(numero)
    
    if numero == 6:
        dollars = dollars + 5
    elif numero == 1:
        dollars = dollars + 1
    else:
        dollars = dollars -2
        
    n = n + 1
        
print("tirada",n,"=",numero, end=" ")
print(" dollars = ", dollars)

