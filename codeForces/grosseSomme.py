somme = 0
n = int(input())
a = list(map(int, input().split()))
for x in range(len(a)):
    if a[x] == a[-1]:
        break
    for y in a:
        somme = somme + (a[x] * a[x+1])
print(somme + 1)