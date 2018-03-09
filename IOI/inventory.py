prices = [0] * 10
nbOperations = int(input())
for x in range(nbOperations):
    number = int(input())
    quantity = int(input())
    prices[number - 1] += quantity
for y in range(10):
    print(prices[y])    