#RO_Pag180_exercici_4.py

from random import randint

def sumad(n):
    a = n % 10
    b = n // 10
    c = a + b
    return(c)
    

sum_max = 0
sum_m = 0
maxs = 0
    
for i in range(1, 11):
    m = randint(1,101)
    sum_m = sumad(m)
    if sum_m > sum_max:
        sum_max = sum_m
        maxs = m
print(sum_max)
print(maxs)
        
        
        
        
        
        
        