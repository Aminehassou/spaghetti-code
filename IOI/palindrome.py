def isPalindrome(phrase):
    reversedPhrase = ""
    for x in range(len(phrase)-1, -1, -1):
        reversedPhrase += phrase[x]
    if phrase == reversedPhrase:
        return True
    return False

nBooks = int(input())

for x in range(nBooks):
    phrase = input()
    phraselower = (phrase.lower()).replace(" ", "")
    if isPalindrome(phraselower):
        print(phrase)

