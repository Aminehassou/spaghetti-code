letter = input()
nLines = int(input())
letterCount = 0
for x in range(nLines):
    line = input()
    for y in line:
        if y == letter:
            letterCount+=1
print(letterCount)
