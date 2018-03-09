nPeople = int(input())
fortunes = [0] * nPeople
for x in range(nPeople):
    money = int(input())
    fortunes[x] = money
fortunes.sort()
if nPeople % 2 == 1:
    index = (nPeople-1) // 2
    print(fortunes[index])
else:
    middle = (fortunes[nPeople//2] + fortunes[(nPeople//2)-1]) / 2
    print(middle)


