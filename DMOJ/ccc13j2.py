word = input()
trueLetters = ("I", "O", "S", "H", "Z", "X", "N")
if any(letter not in word for letter in trueLetters):
    print("NO")
else:
    print("YES")
