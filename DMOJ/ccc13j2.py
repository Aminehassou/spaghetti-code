word = input()
trueLetters = ("I", "O", "S", "H", "Z", "X", "N")
if any(letter not in trueLetters for letter in word):
    print("NO")
else:
    print("YES")
