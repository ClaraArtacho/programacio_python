#RO_Pag147_exercici_14_articles_1.py

#for n i range (0, 4):


diners = 1000
articles = [482, 888, 727, 654]
articles_comprar = 0

for n in range(0,4):
    if diners >= articles[n]:
        articles_comprar = articles_comprar + 1
        print("podem comprar " , diners//articles[n], "unitats de l'article ", n + 1)
    if n == len(articles)-1:
        
        print("articles que podem comprar = ", articles_comprar)
    