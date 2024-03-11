#RO_Pag025_execicio5.py

examen = float(input("examen = ")) #nota sobre 100
lliso = float(input("lliso = ")) #nota sobre 10
a = float(input("a ="))
b = float(input("b ="))
c = float(input("c ="))


mitjanatasca = (a + b + c) / 3

notatotal = (examen * 0.7) + (lliso * 2) + (mitjanatasca * 1)

print("notatotal = ", notatotal)
print("examen * 0.7 = ", examen * 0.7)
print("lliso * 2 = ", lliso * 2)
print("mitjanatasca * 1 = ", mitjanatasca * 1)
