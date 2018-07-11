names = list(input().split(" "))
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
kid1 = 0
kid2 = 0
for letter in names[0]:
    number = alphabet.find(letter)
    kid1 += number
for letter in names[1]:
    number = alphabet.find(letter)
    kid2 += number
while kid1 >= 10:
    kid1 = str(kid1)
    kid1 = list(map(int, kid1))
    kid1 = sum(kid1)
while kid2 >= 10:
    kid2 = str(kid2)
    kid2 = list(map(int, kid2))
    kid2 = sum(kid2)
print(kid1, kid2)