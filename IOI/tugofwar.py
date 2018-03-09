pEq1 = 0
pEq2 = 0
nbMembres = int(input())
for x in range(nbMembres):
    poids = int(input())
    pEq1 += poids
    poids = int(input())
    pEq2 += poids
if pEq1 > pEq2:
    print("L'équipe 1 a un avantage")
else:
    print("L'équipe 2 a un avantage")
print("Poids total pour l'équipe 1 : ", pEq1)
print("Poids total pour l'équipe 2 : ", pEq2)

