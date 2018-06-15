def isAmerican(word):
    vowels = ["a", "e", "i", "o", "u", "y"]
    if (len(word) > 4) and (word[-3] not in vowels) and (word[-2] == "o") and (word[-1] == "r"):
        for letter in word:
            print(letter, end = "")
            if letter == "o":
                print("u", end = "")
    elif word == "quit!":
        return False
    else:
        print(word, end = "")
    print()
word = 0
canada = 6
while canada != False:
    word = input()
    canada = isAmerican(word)
