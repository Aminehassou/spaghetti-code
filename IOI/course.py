nPeople = int(input())
integers = [0] * nPeople
for x in range(nPeople):
    integer = int(input())
    integers[x] = integer
integers.sort()
for y in range(1, (nPeople//2)+1):
    print("{} {}".format(integers[y-1], integers[nPeople-y] ))