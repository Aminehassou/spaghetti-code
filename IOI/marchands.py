nbMarchands = int(input())
minCost = 1000000
position = 0
for x in range(1, nbMarchands + 1):
    price = int(input())
    if price <= minCost:
        minCost = price
        position = x
print(position)