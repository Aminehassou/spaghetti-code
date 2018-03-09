numbers = []
listSize = int(input())
for x in range(listSize):
    number = int(input())
    numbers.append(number)
numbers.sort()
for x in numbers:
    print(x)
