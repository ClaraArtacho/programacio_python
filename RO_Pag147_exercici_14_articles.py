#RO_Pag147_exercici_14_articles.py

#for n i range (0, 4):

n = 4
articles = [1454, 904, 634, 2933]
preu = [float(input("Introdueix el preu de l'article: ")) for i in range(n)]
diners = float(input("Introdueix els diners disponibles: "))
articles_comprar = 0

for i in range (1, n + 1):
    if preu <= diners:
        articles_comprar = articles_comprar + 0
        print("Resultat de articles que pots comprar: ", articles_comprar)
    else:
        articles_comprar = articles_comprar + 1
        print("Resultat de articles que pots comprar: ", articles_comprar)
            
            