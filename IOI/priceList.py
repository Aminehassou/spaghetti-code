prices = [9, 5, 12, 15, 7, 42, 13, 10, 1, 20]
fPrice = 0
for x in range(10):
    weight = int(input())
    fPrice += weight * prices[x]
print(fPrice)
