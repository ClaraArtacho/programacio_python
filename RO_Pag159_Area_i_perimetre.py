#RO_Pag159_Area_i_perimetre.py

from math import*

def cuadrado(a):
    A = a**2
    P = 4 * a
    print("Area = ", A)
    print("Perimetre = ",P)
    
def triangulo(a,b,c,h):
    A = (b * h) / 2
    P = a + b + c
    print("Area = ", A)
    print("Perimetre = ",P)
    
def rectangulo(a,b):
    A = b * a
    P = 2 * (b + a)
    print("Area = ", A)
    print("Perimetre = ",P)
    
def rombo(D,d,a):
    A = (D * d) / 2
    P = 4 * a
    print("Area = ", A)
    print("Perimetre = ",P)
    
def paralelogramo(b,h,a):
    A = b * h
    P =2 * (b + a)
    print("Area = ", A)
    print("Perimetre = ",P)
    
def cometa(D,d,b,a):
    A = (D * d) / 2
    P = 2 * (b + a)
    print("Area = ", A)
    print("Perimetre = ",P)
    
def trapecio(B,b,h,c,a):
    A = ((B + b)* h) / 2
    P = B + b + a + c
    print("Area = ", A)
    print("Perimetre = ",P)
    
def circulo(pi,r):
    A = pi * r**2
    P = 2 * pi * r
    print("Area = ", A)
    print("Perimetre = ",P)
    
def poligano_regular(P,a,n,b):
    A = (P * a) / 2
    P = n * b
    print("Area = ", A)
    print("Perimetre = ",P)
    
def corona_circular(pi,R,r):
    A = pi * ((R**2) - (r**2))
    print("Area = ", A)
    
def sector_circular(pi,R,n):
    A = (pi * R**2 * n) / 360
    print("Area = ", A)
    
def cubo(a):
    A = 6 * a**2
    V = a**3
    print("Area = ", A)
    print("Volum = ", V)
    
def cilindrio(pi,R,h):
    A = 2 * pi * R * (h+R)
    V = pi * h * R**2
    print("Area = ", A)
    print("Volum = ", V)
    
def ortoedro(a,b,c):
    A = 2 * ((a * b) + (a * c) + (b * c))
    V = a * b * c
    print("Area = ", A)
    print("Volum = ", V)
    
def prisma_recto(P,h,a,Ab):
    A = P * (h + a)
    V = Ab * h
    # P = peímetro de la base
    # Ab = àrea de la base
    # a = apotema base
    print("Area = ", A)
    print("Volum = ", V)
    
def cono(pi,R,g,h,pi):
    A = pi * R * (R * g)
    V = (pi * R**2 * h) / 3
    # g = generatriz
    print("Area = ", A)
    print("Volum = ", V)
    
def tronco_de_cono(pi,g,r,R,h):
    A = pi * ((g * (r+ R) + r**2 + R**2))
    V = (pi * h * ( R**2 + r**2 + (R * r))) / 3
    print("Area = ", A)
    print("Volum = ", V)
    
def esfera(pi,R):
    A = 4 * pi * R**2
    V = (4 * pi * R**3) / 3
    print("Area = ", A)
    print("Volum = ", V)
    
def piramide(P,a,aa,h,Ab):
    A = (P * (a + aa)) / 2
    V = (Ab * h)/ 3
    print("Area = ", A)
    print("Volum = ", V)
    
def tetraedro_regular(a):
    A = sqrt(3) * a**2
    V = (sqrt(2) * a**3) / 12
    print("Area = ", A)
    print("Volum = ", V)
    
def octaedro_regular(a):
    A = 2 * sqrt(3) * a**2
    V = (sqrt(2) *  a**3) / 3
    print("Area = ", A)
    print("Volum = ", V)
    
def tronco_de_piramide(P,PP,a,Ab,AAb,h):
    A = ((P + PP) / 2) * a + Ab + AAb
    V = ((Ab + AAb * sqrt(Ab * AAb)) * h) / 3
    # P, PP = perimetres de les bases
    # Ab, AAb = areas de les bases
    print("Area = ", A)
    print("Volum = ", V)
    
def casquete_esférico(pi,R,h):
    A = 2 * pi * R * h
    V = ( pi * h**2 * ((3 * R) - h)) / 3
    print("Area = ", A)
    print("Volum = ", V)
    
def cuña_esferica(pi,R,ñ):
    A = (4 * pi* R**2 * ñ) / 360
    V = (4 * pi * R**3 * ñ) / (3 * 360)
    print("Area = ", A)
    print("Volum = ", V)
    
def segmento_esferico(pi,R,h,r,rr):
    A = 2 * pi * R * h
    V = (pi *h* (h**2 + (3 * r**2) + (3 * rr**2))) / 6
    print("Area = ", A)
    print("Volum = ", V)



# Programa principal main
sortida= False
while not sortida:
    print("")
    print("calcul d'arees, volums i perimetres")
    print("Escull la figura a calcular = ")
    print("1. cuadrado")
    print("2. triangulo")
    print("3. rectangulo")
    print("4. paralelogramo")
    print("5. rombo")
    print("6. cometa")
    print("7. trapecio")
    print("8. circulo")
    print("9. poligano regular")
    print("10. corona circular")
    print("11. sector circular")
    print("12. cubo")
    print("13. cilindrio")
    print("14. ortoedro")
    print("15. prisma recto")
    print("16. cono")
    print("17. tronco de cono")
    print("18. esfera")
    print("19. piramide")
    print("20. tetraedro regular")
    print("21. octaedro regular")
    print("22. tronco de piramide")
    print("23. casquete esferico")
    print("24. huso: cuña esferica")
    print("25. zonao segmento esferico")
    
    opcio = int(input("Escull una opcio: "))
    
    if opcio == 1:
        a = float(input("Introdueix el costat: "))
        cuadrado(a)
    
    elif opcio == 2:
        a = float(input("Introdueix el costat: "))
        b = float(input("Introdueix el costat: "))
        c = float(input("Introdueix el costat: "))
        h = float(input("Introdueix l'altura: "))
        triangulo(a,b,c,h)
    
    elif opcio == 3:
        a = float(input("Introdueix el costat: "))
        b = float(input("Introdueix el costat: "))
        rectangulo(a,b)
        
    elif opcio == 4:
        a = float(input("Introdueix el costat: "))
        b = float(input("Introdueix el costat: "))
        h = float(input("Introdueix l'altura: "))
        rombo(D,d,a)
    
    elif opcio == 5:
        a = float(input("Introdueix el costat: "))
        d = float(input("Introdueix el costat: "))
        D = float(input("Introdueix el costat: "))
        paralelogramo(b,h,a)
    
    elif opcio == 6:
        a = float(input("Introdueix el costat: "))
        b = float(input("Introdueix el costat: "))
        d = float(input("Introdueix el costat: "))
        D = float(input("Introdueix el costat: "))
        cometa(D,d,b,a)
        
    elif opcio == 7:
        a = float(input("Introdueix el costat: "))
        b = float(input("Introdueix el costat: "))
        c = float(input("Introdueix el costat: "))
        h = float(input("Introdueix l'altura: "))
        B = float(input("Introdueix el costat: "))
        trapecio(B,b,h,c,a)
        
    elif opcio == 8:
        r = float(input("Introdueix el radi: "))
        pi = 3,14
        circulo(pi,r)
        
    elif opcio == 9:
        a = float(input("Introdueix l'apotema: "))
        b = float(input("Introdueix el costat: "))
        n = float(input("Introdueix el num de costats: "))
        poligano_regular(P,a,n,b)
        
    elif opcio == 10:
        r = float(input("Introdueix el radi petit: "))
        R = float(input("Introdueix el radi gran: "))
        pi = 3,14
        corona_circular(pi,R,r)
        
    elif opcio == 11:
        R = float(input("Introdueix el radi: "))
        n = float(input("Introdueix els graus: "))
        pi = 3,14
        sector_circular(pi,R,n)
        
    elif opcio == 12:
        a = float(input("Introdueix el costat: "))
        cubo(a)
        
    elif opcio == 13:
        R = float(input("Introdueix el radi: "))
        h = float(input("Introdueix el costat: "))
        pi = 3,14
        cilindrio(pi,R,h)
        
    elif opcio == 14:
        a = float(input("Introdueix el costat: "))
        b = float(input("Introdueix el costat: "))
        c = float(input("Introdueix el costat: "))
        ortoedro(a,b,c)
        
    elif opcio == 15:
        a = float(input("Introdueix el costat: "))
        P = float(input("Introdueix el costat: "))
        h = float(input("Introdueix el costat: "))
        Ab = float(input("Introdueix el costat: "))
        prisma_recto(P,h,a,Ab)
        
    elif opcio == 16:
        R = float(input("Introdueix el radi: "))
        h = float(input("Introdueix l'altura: "))
        a = float(input("Introdueix el costat: "))
        g = float(input("Introdueix el generatriz: "))
        pi = 3,1416
        cono(pi,R,g,h,pi)
    
    
    elif opcio == 17:
        h = float(input("Introdueix l'altura: "))
        r = float(input("Introdueix el radi petit: "))
        R = float(input("Introdueix el radi gran: "))
        pi = 3,1416
        g = float(input("Introdueix el generatriz: "))
        tronco_de_cono(pi,g,r,R,h)
        
    elif opcio == 18:
        R = float(input("Introdueix el radi gran: "))
        pi = 3,1416
        esfera(pi,R)
        
    elif opcio == 19:
        P = float(input("Introdueix el perimetre de la base: "))
        a = float(input("Introdueix el costat: "))
        aa = float(input("Introdueix el costat: "))
        h = float(input("Introdueix l'altura: "))
        Ab = float(input("Introdueix l'area de la base: "))
        piramide(P,a,aa,h,Ab)
        
    elif opcio == 20:
        a = float(input("Introdueix el costat: "))
        tetraedro_regular(a)
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    