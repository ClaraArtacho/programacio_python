#RO_Pag180_exercici_2.py

from random import randint

def primo(n):
    m = 0
    for i in range (1, n + 1):
        if n % i == 0:
            m = m + 1
            if m < 2:
                return m

for n in range(1,2):
    a = randint(1,100)
    b = primo(n)
print(b)
    
        