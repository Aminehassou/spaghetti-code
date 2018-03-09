line = input()
characters = list(line)
for x in range(len(line)):
    if characters[x] == " ":
        characters[x] = "_"
line = "".join(characters)
print(line)