

amplada = float(input("introdueix l'amplada en metres = "))
altura = float(input("introdueix l'altura en metres = "))
profunditat = float(input("introdueix la profunditat = "))

area = 2 * (amplada * profunditat + altura * amplada + profunditat * altura)
volum = (amplada * altura * profunditat)

print("area =", area)
print("volum =", volum)