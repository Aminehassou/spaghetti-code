nbProduits = int(input())
nbPersonnes = int(input())
favProducts = [0] * nbProduits
for x in range(nbPersonnes):
    product = int(input())
    favProducts[product] += 1
for x in favProducts:
    print(x)

