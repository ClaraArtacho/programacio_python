#RO_Pag181_exercici_13.py

from math import*

def cartesiana(r,t):
    x = r * cos(t)
    y = r * sin(t)
    print(x)
    print(y)
    
def polar(x,y):
    r = sqrt((pow(x,2) + (pow(y,2))))
    t = atan(y / x)
    print(r)
    print(t)

sortida = False
while not sortida:
    print("")
    print("1. Convertir a polares")
    print("2. Convertir a cartesianas")
    print("3. Salir")
    print("")

    opcio = int(input("escull una opció: "))
    
    if opcio == 1:
        x = int(input("introdueix costat: "))
        y = int(input("introdueix costat: "))
        cartesiana(r,t)
        print("Coordenades polars: ",cartesiana)
        
    elif opcio == 2:
        r = int(input("introdueix hipotenusa: "))
        t = int(input("introdueix angle en radians: "))
        polar(x,y)
        print("Coordenades cartesianes: ", polar)
    
    else:
        if opcio == 3:
            print("Sortint del programa")
        
        
        
        