#RO_Pag105_Ulam.py


x = int(input("Introdueix la dada inicial: "))

while x > 1:
    if x % 2 == 0:
        x = x // 2
        print(x)

    else:
        x = (3 * x) + 1
        print(x)
