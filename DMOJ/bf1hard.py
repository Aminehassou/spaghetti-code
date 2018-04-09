numbers = []
listSize = int(input())
for x in range(listSize):
    numbers.append(int(input()))
sortedNumbers = sorted(numbers)
for number in sortedNumbers:
    print(number)
