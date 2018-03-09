v1 = int(input())
v2 = int(input())
sum = v1 + v2
if sum >= 10:
    print("Taxe spéciale !")
    print(36)
else:
    print("Taxe régulière")
    print(sum * 2)