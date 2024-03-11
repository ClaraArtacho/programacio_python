#RO_Pag148_exercici_21.py


from random import*

pos_rana = 10
cont = 0

while (pos_rana > o and pos_rana < 20):
    aleatori = random.randint(0,1)
    if aleatori == 0:
        salt =-1
    else:
        salt = 1
        
        pos_rana = pos_rana + salt
        cont = cont + 1;
        print("posicio granota: ",pos_rana)
    
print
print