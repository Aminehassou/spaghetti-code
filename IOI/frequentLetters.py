from string import ascii_lowercase, ascii_uppercase
alphabet = ascii_lowercase
phrase = input("Enter phrase here: ")
maxCount = 0
winner = ""
#Checks for highest recurring letter in the phrase
for letter in alphabet:
    if (phrase.count(letter) + phrase.count(letter.upper())) > maxCount:
        maxCount = phrase.count(letter) + phrase.count(letter.upper())
        winner = letter
print(winner.upper())


    